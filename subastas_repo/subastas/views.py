from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse, reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.views.generic import CreateView
from django.views.generic import ListView
from django.views.generic import UpdateView
from django.views.generic import FormView

from braces.views import LoginRequiredMixin

from personas.forms import PersonaForm
from personas.models import Persona
from .forms import ActaForm, SubastaForm
from .models import Acta, Subasta


@login_required
def home(request):
    if request.user.groups.filter(name="administradores").exists():
        url = 'subastas:list'
    elif request.user.groups.filter(name="acreditadores").exists():
        url = 'subastas:acreditadores'
    elif request.user.groups.filter(name="acteros").exists():
        url = 'subastas:actas'

    return redirect(reverse(url))


class SubastaListView(LoginRequiredMixin, ListView):
    current_subasta = Subasta.current
    model = Subasta
    template_name = 'subastas/list.html'

    def get_queryset(self):
        return Subasta.objects.filter(cerrado_el__lt=timezone.now())

    def get_context_data(self, **kwargs):
        context = super(SubastaListView, self).get_context_data(**kwargs)
        context['current'] = self.current_subasta
        return context


class SubastaCreateView(LoginRequiredMixin, CreateView):
    form_class = SubastaForm
    model = Subasta
    success_url = reverse_lazy('subastas:list')
    template_name = 'subastas/form.html'

    def form_valid(self, form):
        messages.add_message(self.request,
                             messages.INFO,
                             'Subasta creada exitosamente.')
        return super(SubastaCreateView, self).form_valid(form)


class SubastaEditView(LoginRequiredMixin, UpdateView):
    context_object_name = 'instance'
    form_class = SubastaForm
    model = Subasta
    success_url = reverse_lazy('subastas:list')
    template_name = 'subastas/form.html'


def cerrar_subasta(request, subasta_id):
    subasta = get_object_or_404(Subasta, pk=subasta_id)
    subasta.cerrado_el = timezone.now()
    subasta.save()
    messages.add_message(request,
                         messages.INFO,
                         'Subasta cerrada exitosamente.')
    return redirect(reverse_lazy("subastas:list"))


class ActaListView(LoginRequiredMixin, ListView):
    current_subasta = Subasta.current
    model = Acta
    template_name = 'subastas/actas/list.html'

    def get_queryset(self):
        if self.current_subasta:
            return Acta.objects.exclude(
                id__in=self.current_subasta.actas.values_list('id', flat=True))
        else:
            return None

    def get_context_data(self, **kwargs):
        context = super(ActaListView, self).get_context_data(**kwargs)
        if self.current_subasta:
            context['current_subasta'] = self.current_subasta
            context['currents'] = self.current_subasta.actas.all()
        return context


class ActaCreateView(LoginRequiredMixin, CreateView):
    form_class = ActaForm
    model = Acta
    template_name = 'subastas/actas/form.html'
    success_url = reverse_lazy('subastas:actas_list')


class AcreditadorHomeView(LoginRequiredMixin, FormView):
    current_subasta = Subasta.current
    form_class = PersonaForm
    model = Persona
    success_url = reverse_lazy('subastas:acreditadores')
    template_name = 'subastas/acreditador_home.html'

    def get_context_data(self, **kwargs):
        context = super(AcreditadorHomeView, self).get_context_data(**kwargs)
        if self.current_subasta:
            context['current_subasta'] = self.current_subasta
            context['personas'] = self.current_subasta.personas.all() \
                .order_by('apellidos')
            context['personas_all'] = Persona.objects.exclude(
                id__in=self.current_subasta.personas.values_list('id', flat=True))

            context['tab'] = self.request.GET.get('tab', 'add')
        return context

    def form_valid(self, form):
        persona_acreditada = form.save()
        self.current_subasta.personas.add(persona_acreditada)
        messages.add_message(self.request,
                             messages.INFO,
                             'Inscripcion exitosa.')
        return redirect(reverse_lazy("subastas:acreditadores"))
