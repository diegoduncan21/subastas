from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils import timezone
from django.views.generic import CreateView
from django.views.generic import ListView

from braces.views import LoginRequiredMixin

from .forms import SubastaForm
from .models import Subasta


@login_required
def home(request):
    if request.user.user_permissions.filter(codename="administrador").exists():
        template = 'subastas/administrador_home.html'
    elif request.user.user_permissions.filter(codename="acreditador").exists():
        template = 'subastas/acreditador_home.html'
    elif request.user.user_permissions.filter(codename="actero").exists():
        template = 'subastas/actero_home.html'

    return render(request, template)


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

    def form_valid(self, form):
        return super(SubastaListView, self).form_valid(form)
