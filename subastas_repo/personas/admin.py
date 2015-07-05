from django.contrib import admin

from .models import Domicilio, Localidad, Persona, Profesional, Titulo

admin.site.register(Domicilio)
admin.site.register(Localidad)
admin.site.register(Persona)
admin.site.register(Profesional)
admin.site.register(Titulo)
