from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import ListView
from django.views.generic import UpdateView
from django.shortcuts import get_object_or_404, render, redirect

from braces.views import LoginRequiredMixin

from subastas.forms import InscriptionForm
from subastas.models import Subasta
from .models import Persona, Profesional


@login_required
def asociar(request, subasta_id):
    if request.method == "POST":
        form = InscriptionForm(request.POST)
        if form.is_valid():
            form.save()
        messages.add_message(request,
                             messages.INFO,
                             msg)
    return redirect(reverse_lazy('subastas:acreditadores')+'?tab=search')


@login_required
def desasociar(request, subasta_id, persona_id):
    subasta = get_object_or_404(Subasta, pk=subasta_id)
    persona = get_object_or_404(Persona, pk=persona_id)
    subasta.personas.remove(persona)
    messages.add_message(request,
                         messages.INFO,
                         'Se borro la inscripcion exitosamente.')
    return redirect(reverse_lazy('subastas:acreditadores')+'?tab=search')


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
