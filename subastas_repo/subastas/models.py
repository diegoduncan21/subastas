from django.db import models
from django.utils import timezone

from openpyxl import load_workbook


class RodadoManager(models.Manager):
    def load_bienes(self, path_xlsx):
        wb = load_workbook(path_xlsx)
        ws = wb.active
        instances = []
        for row in ws.iter_rows(range_string="A2:K3"):
            subasta = Subasta.objects.create(numero_inventario=row[0],
                                             descripcion=row[4],
                                             modelo=row[8],
                                             chasis=row[9],
                                             motor=row[10],
                                             dominio=row[6])
            instances.append(subasta)
        return len(instances)


class Rodado(models.Model):
    numero_inventario = models.IntegerField()
    descripcion = models.TextField(blank=True, null=True)
    modelo = models.IntegerField()
    chasis = models.CharField(max_length=15)
    motor = models.CharField(max_length=10)
    dominio = models.CharField(max_length=12)
    precio_base = models.FloatField(default=0)
    precio_venta = models.FloatField(default=0)
    lote = models.IntegerField(default=0)
    chatarra = models.BooleanField(default=False)

    def __unicode__(self):
        return "%s %s %s" % (self.chasis, self.motor, self.dominio)


class SubastaManager(models.Manager):
    def get_current(self):
        return super(SubastaManager, self).get_queryset() \
            .filter(fecha_hora__day=timezone.now().day,
                    cerrado_el=None).last()


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

    objects = SubastaManager()

    def __unicode__(self):
        return "%s %s" % (self.numero, self.decreto)

    def close(self):
        self.cerrado_el = timezone.now()
        self.save()


class Acta(models.Model):
    bien_rodado = models.ForeignKey(Rodado)
    persona = models.ForeignKey('personas.Persona')
    profesionales = models.ManyToManyField('personas.Profesional')
    descripcion = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return "%s %s" % (self.bien_rodado, self.persona)
