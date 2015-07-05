from django.contrib import admin

from .models import Acta, Grupo, Lote, Rodado, Subasta, Tipo


class ActaAdmin(admin.ModelAdmin):
    filter_horizontal = ('profesionales', )


class RodadoAdmin(admin.ModelAdmin):
    list_display = [
        "lote",
        "tipo",
        "numero_inventario",
        "descripcion",
        "modelo",
        "chasis",
        "motor",
        "dominio",
        "marca",
        "anio",
        "precio_base",
        "precio_venta",
        "subastado",
    ]


class SubastaAdmin(admin.ModelAdmin):
    list_display = [
        'numero',
        'fecha_hora',
        'cerrado_el',
        'decreto',
        'domicilio',
    ]
    filter_horizontal = ('personas', 'profesionales')

admin.site.register(Acta, ActaAdmin)
admin.site.register(Grupo)
admin.site.register(Lote)
admin.site.register(Rodado, RodadoAdmin)
admin.site.register(Subasta, SubastaAdmin)
admin.site.register(Tipo)
