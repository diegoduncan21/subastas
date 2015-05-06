from django.contrib import admin

from .models import Acta, Caracteristica, Rodado, Subasta


class ActaAdmin(admin.ModelAdmin):
    filter_horizontal = ('profesionales', )


class SubastaAdmin(admin.ModelAdmin):
    filter_horizontal = ('actas', 'bienes', 'personas', 'profesionales')

admin.site.register(Acta, ActaAdmin)
admin.site.register(Caracteristica)
admin.site.register(Rodado)
admin.site.register(Subasta, SubastaAdmin)
