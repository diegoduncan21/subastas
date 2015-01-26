from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def home(request):

    if request.user.user_permissions.filter(codename="administrador").exists():
        template = 'subastas/administrador_home.html'
    elif request.user.user_permissions.filter(codename="acreditador").exists():
        template = 'subastas/acreditador_home.html'
    elif request.user.user_permissions.filter(codename="actero").exists():
        template = 'subastas/actero_home.html'

    return render(request, template)
