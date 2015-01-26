from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def home(request):

    if request.user.user_permissions.filter(codename="administrador").exists():
        template = 'subastas/administrador.html'
    elif request.user.user_permissions.filter(codename="acreditador").exists():
        template = 'subastas/acreditador.html'
    elif request.user.user_permissions.filter(codename="actero").exists():
        template = 'subastas/actero.html'

    return render(request, template)
