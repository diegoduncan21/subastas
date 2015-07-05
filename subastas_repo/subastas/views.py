from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse, reverse_lazy
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.views.generic import CreateView
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic import UpdateView
from django.views.generic import FormView

from braces.views import LoginRequiredMixin

from personas.forms import PersonaForm
from personas.models import Persona
from .forms import (ActaForm,
                    GrupoForm,
                    InscriptionForm,
                    LoteForm,
                    RodadoForm,
                    SubastaForm)
from .models import (Acta,
                     Grupo,
                     Lote,
                     Rodado,
                     Subasta)


@login_required
def home(request):
    if request.user.groups.filter(name="administradores").exists():
        url = 'subastas:list'
    elif request.user.groups.filter(name="acreditadores").exists():
        url = 'subastas:acreditadores'
    elif request.user.groups.filter(name="acteros").exists():
        url = 'subastas:actas'
    else:
        url = 'subastas:sin_permisos'

    return redirect(reverse(url))


class SubastaListView(LoginRequiredMixin, ListView):
    model = Subasta
    template_name = 'subastas/list.html'

    def get_queryset(self):
        """Subastas anteriores o cerradas"""
        return Subasta.objects.filter(Q(cerrado_el__lt=timezone.now()) |
                                      Q(fecha_hora__lt=timezone.now())) \
                              .exclude(fecha_hora__day=timezone.now().day)

    def get_context_data(self, **kwargs):
        context = super(SubastaListView, self).get_context_data(**kwargs)
        context['current'] = Subasta.objects.get_current()
        next_subastas = Subasta.objects.filter(fecha_hora__gt=timezone.now()) \
                                       .exclude(fecha_hora__day=timezone.now().day)
        context['next_subastas'] = next_subastas
        return context


class SubastaCreateView(LoginRequiredMixin, CreateView):
    form_class = SubastaForm
    model = Subasta
    success_url = reverse_lazy('subastas:list')
    template_name = 'subastas/form.html'

    def form_valid(self, form):
        form.save()
        messages.add_message(self.request,
                             messages.INFO,
                             'Subasta creada exitosamente.')
        return super(SubastaCreateView, self).form_valid(form)


class SubastaUpdateView(LoginRequiredMixin, UpdateView):
    context_object_name = 'instance'
    form_class = SubastaForm
    model = Subasta
    success_url = reverse_lazy('subastas:list')
    template_name = 'subastas/form.html'

    def form_valid(self, form):
        messages.add_message(self.request,
                             messages.INFO,
                             'Subasta modificada exitosamente.')
        return super(SubastaUpdateView, self).form_valid(form)


def cerrar_subasta(request, subasta_id):
    subasta = get_object_or_404(Subasta, pk=subasta_id)
    subasta.cerrado_el = timezone.now()
    subasta.save()
    messages.add_message(request,
                         messages.INFO,
                         'Subasta cerrada exitosamente.')
    return redirect(reverse_lazy("subastas:list"))


class ActaListView(LoginRequiredMixin, ListView):
    model = Acta
    template_name = 'subastas/actas/list.html'

    def get_queryset(self):
        self.current_subasta = Subasta.objects.get_current()
        if self.current_subasta:
            return self.current_subasta.actas.all()
        else:
            return None

    def get_context_data(self, **kwargs):
        self.current_subasta = Subasta.objects.get_current()
        context = super(ActaListView, self).get_context_data(**kwargs)
        if self.current_subasta:
            context['current_subasta'] = self.current_subasta
        return context


class ActaCreateView(LoginRequiredMixin, CreateView):
    form_class = ActaForm
    model = Acta
    template_name = 'subastas/actas/form.html'
    success_url = reverse_lazy('subastas:actas')

    def form_valid(self, form):
        acta_nueva = form.save(commit=False)
        acta_nueva.subasta = Subasta.objects.get_current()
        acta_nueva.save()
        messages.add_message(self.request,
                             messages.INFO,
                             'Acta agregada exitosamente.')
        return super(ActaCreateView, self).form_valid(form)


class ActaPrintView(LoginRequiredMixin, DetailView):
    model = Acta
    template_name = 'subastas/actas/print.html'

    def get_context_data(self, **kwargs):
        context = super(ActaPrintView, self).get_context_data(**kwargs)
        acta = kwargs.get('object')
        context['bienes'] = Rodado.objects.filter(lote=acta.lote)
        return context


class AcreditadorHomeView(LoginRequiredMixin, FormView):
    form_class = PersonaForm
    model = Persona
    success_url = reverse_lazy('subastas:acreditadores')
    template_name = 'subastas/acreditador_home.html'

    def get_context_data(self, **kwargs):
        self.current_subasta = Subasta.objects.get_current()
        context = super(AcreditadorHomeView, self).get_context_data(**kwargs)
        if self.current_subasta:
            context['current_subasta'] = self.current_subasta
            context['personas'] = self.current_subasta.personas.all() \
                .order_by('apellidos')

            query = self.request.GET.get('q', '')
            context['form_inscriptions'] = InscriptionForm(
                instance=self.current_subasta, query=query)

            context['tab'] = self.request.GET.get('tab', 'search')
            context['query'] = query
        return context

    def form_valid(self, form):
        self.current_subasta = Subasta.objects.get_current()
        persona_acreditada = form.save()
        self.current_subasta.personas.add(persona_acreditada)
        messages.add_message(self.request,
                             messages.INFO,
                             'Inscripcion exitosa.')
        return redirect(reverse_lazy("subastas:acreditadores"))

    def form_invalid(self, form):
        return super(AcreditadorHomeView, self).form_invalid(form)


class RodadoListView(LoginRequiredMixin, ListView):
    model = Rodado
    template_name = 'subastas/rodados/list.html'

    def get_queryset(self):
        """Bienes sin subastar"""
        return Rodado.objects.no_subastados()

    def get_context_data(self, **kwargs):
        context = super(RodadoListView, self).get_context_data(**kwargs)
        context['current_subasta'] = Subasta.objects.get_current()
        return context


class RodadoCreateView(LoginRequiredMixin, CreateView):
    form_class = RodadoForm
    model = Rodado
    template_name = 'subastas/rodados/form.html'
    success_url = reverse_lazy('subastas:rodados')

    def form_valid(self, form):
        messages.add_message(self.request,
                             messages.INFO,
                             'Bien cargado exitosamente.')
        return super(RodadoCreateView, self).form_valid(form)


class RodadoUpdateView(LoginRequiredMixin, UpdateView):
    context_object_name = 'instance'
    form_class = RodadoForm
    model = Rodado
    success_url = reverse_lazy('subastas:rodados')
    template_name = 'subastas/rodados/form.html'

    def form_valid(self, form):
        messages.add_message(self.request,
                             messages.INFO,
                             'Bien modificado exitosamente.')
        return super(RodadoUpdateView, self).form_valid(form)


def upload_xlsx(request):
    if request.method == "POST":
        rodados_cargados = Rodado.objects \
            .load_bienes(request.FILES['bienes_file'])
        messages.add_message(request,
                             messages.INFO,
                             'Bienes cargados: %s' % (rodados_cargados))
    return render(request, 'subastas/rodados/cargar_xlsx.html')


class GrupoListView(LoginRequiredMixin, ListView):
    model = Grupo
    template_name = 'subastas/grupos/list.html'

    def get_queryset(self):
        """Grupos de la subasta vigente"""
        subasta = Subasta.objects.get_current()
        return subasta.grupos.all()


class GrupoDetailView(LoginRequiredMixin, DetailView):
    model = Grupo
    template_name = 'subastas/grupos/detail.html'


class GrupoCreateView(LoginRequiredMixin, CreateView):
    form_class = GrupoForm
    model = Grupo
    template_name = 'subastas/grupos/form.html'
    success_url = reverse_lazy('subastas:grupos')

    def form_valid(self, form):
        grupo = form.save(commit=False)
        grupo.subasta = Subasta.objects.get_current()
        grupo.save()
        messages.add_message(self.request,
                             messages.INFO,
                             'Grupo cargado exitosamente.')
        return super(GrupoCreateView, self).form_valid(form)

    def form_invalid(self, form):
        print form.errors
        return super(GrupoCreateView, self).form_invalid(form)


class LoteListView(LoginRequiredMixin, ListView):
    model = Lote
    template_name = 'subastas/lotes/list.html'

    def get_queryset(self):
        """Lotes de la subasta vigente"""
        subasta = Subasta.objects.get_current()
        grupo_id = self.kwargs.get('grupo_id')
        return subasta.grupos.get(id=grupo_id).lotes.all()

    def get_context_data(self, **kwargs):
        context = super(LoteListView, self).get_context_data(**kwargs)
        context['grupo_id'] = self.kwargs.get('grupo_id')
        return context


class LoteDetailView(LoginRequiredMixin, DetailView):
    model = Lote
    template_name = 'subastas/lotes/detail.html'


class LoteCreateView(LoginRequiredMixin, CreateView):
    form_class = LoteForm
    model = Lote
    template_name = 'subastas/lotes/form.html'

    def get_success_url(self):
        return reverse('subastas:lotes', args=(self.kwargs.get('grupo_id'), ))

    def form_valid(self, form):
        lote = form.save(commit=False)
        lote.grupo = Grupo.objects.get(id=self.kwargs.get('grupo_id'))
        lote.save()
        messages.add_message(self.request,
                             messages.INFO,
                             'Lote cargado exitosamente.')
        return super(LoteCreateView, self).form_valid(form)

    def form_invalid(self, form):
        print form.errors
        return super(LoteCreateView, self).form_invalid(form)

    def get_form_kwargs(self):
        kwargs = super(LoteCreateView, self).get_form_kwargs()
        kwargs['grupo_id'] = self.kwargs.get('grupo_id')
        return kwargs
