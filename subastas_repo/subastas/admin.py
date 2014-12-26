from django.contrib import admin

from .models import Actas, Caracteristicas, Rodado, Subasta


class ActaAdmin(admin.ModelAdmin):
    filter_horizontal = ('profesionales', )


class SubastaAdmin(admin.ModelAdmin):
    filter_horizontal = ('actas', 'bienes', 'personas', 'profesionales')

admin.site.register(Actas, ActaAdmin)
admin.site.register(Caracteristicas)
admin.site.register(Rodado)
admin.site.register(Subasta, SubastaAdmin)
