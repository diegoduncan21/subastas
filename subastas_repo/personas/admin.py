from django.contrib import admin

from .models import Domicilio, Localidad, Persona, Profesional

admin.site.register(Domicilio)
admin.site.register(Localidad)
admin.site.register(Persona)
admin.site.register(Profesional)
