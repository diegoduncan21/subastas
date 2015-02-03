from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import ListView
from django.views.generic import UpdateView
from django.shortcuts import render

from braces.views import LoginRequiredMixin

from .models import Profesional


class ProfesionalListView(LoginRequiredMixin, ListView):
    model = Profesional
    template_name = 'personas/profesionales/list.html'

    def get_queryset(self):
        return Profesional.objects.all().order_by('titulo')


class ProfesionalCreateView(LoginRequiredMixin, CreateView):
    model = Profesional
    template_name = 'personas/profesionales/form.html'
    success_url = reverse_lazy('personas:profesionales_list')


class ProfesionalUpdateView(LoginRequiredMixin, UpdateView):
    context_object_name = 'instance'
    model = Profesional
    template_name = 'personas/profesionales/form.html'
    success_url = reverse_lazy('personas:profesionales_list')


class ProfesionalDeleteView(LoginRequiredMixin, DeleteView):
    model = Profesional
    template_name = 'personas/profesionales/confirm_delete.html'
    success_url = reverse_lazy('personas:profesionales_list')
