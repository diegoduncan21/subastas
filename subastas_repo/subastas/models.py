from django.db import models
from django.utils import timezone


class Rodado(models.Model):
    numero_inventario = models.IntegerField()
    caracteristicas = models.ForeignKey("Caracteristica")
    modelo = models.IntegerField()
    chasis = models.CharField(max_length=15)
    motor = models.CharField(max_length=10)
    dominio = models.CharField(max_length=12)
    precio_base = models.FloatField(default=0)
    precio_venta = models.FloatField(default=0)
    lote = models.IntegerField()
    chatarra = models.BooleanField(default=False)

    def __unicode__(self):
        return "%s %s %s" % (self.chasis, self.motor, self.dominio)


class Caracteristica(models.Model):
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    descripcion = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return "%s %s" % (self.marca, self.modelo)


class Subasta(models.Model):
    numero = models.IntegerField()
    fecha_hora = models.DateTimeField()
    cerrado_el = models.DateTimeField(blank=True, null=True)
    decreto = models.CharField(max_length=10)
    domicilio = models.ForeignKey('personas.Domicilio')

    profesionales = models.ManyToManyField('personas.Profesional')
    bienes = models.ManyToManyField(Rodado)
    personas = models.ManyToManyField('personas.Persona',
                                      blank=True, null=True)
    actas = models.ManyToManyField('Acta', blank=True, null=True)

    def __unicode__(self):
        return "%s %s" % (self.numero, self.decreto)

    @classmethod
    def get_current(self):
        return None


class Acta(models.Model):
    bien_rodado = models.ForeignKey(Rodado)
    persona = models.ForeignKey('personas.Persona')
    profesionales = models.ManyToManyField('personas.Profesional')
    descripcion = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return "%s %s" % (self.bien_rodado, self.persona)
