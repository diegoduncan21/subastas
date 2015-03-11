from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse, reverse_lazy
from django.shortcuts import render, redirect
from django.utils import timezone
from django.views.generic import CreateView
from django.views.generic import ListView

from braces.views import LoginRequiredMixin

from .forms import ActasForm, SubastaForm
from .models import Actas, Subasta


@login_required
def home(request):
    if request.user.user_permissions.filter(codename="administrador").exists():
        url = 'subastas:list'
    elif request.user.user_permissions.filter(codename="acreditador").exists():
        url = 'subastas:acreditador_list'
    elif request.user.user_permissions.filter(codename="actero").exists():
        url = 'subastas:actas_list'

    return redirect(reverse(url))


class SubastaListView(LoginRequiredMixin, ListView):
    model = Subasta
    template_name = 'subastas/list.html'

    def get_queryset(self):
        return Subasta.objects.all() \
            .exclude(fecha_hora__day=timezone.now().day)

    def get_context_data(self, **kwargs):
        context = super(SubastaListView, self).get_context_data(**kwargs)
        context['current'] = Subasta.get_current()
        return context


class SubastaCreateView(LoginRequiredMixin, CreateView):
    form_class = SubastaForm
    model = Subasta
    template_name = 'subastas/form.html'
    success_url = reverse_lazy('subastas:list')

    def form_valid(self, form):
        return super(SubastaCreateView, self).form_valid(form)


class ActaListView(LoginRequiredMixin, ListView):
    model = Actas
    template_name = 'subastas/actas/list.html'
    current_subasta = Subasta.get_current()

    def get_queryset(self):
        if self.current_subasta:
            return Actas.objects.exclude(
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
    form_class = ActasForm
    model = Actas
    template_name = 'subastas/actas/form.html'
    success_url = reverse_lazy('subastas:actas_list')
