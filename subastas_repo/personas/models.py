# -*- coding: utf-8 -*-

from django.db import models

from model_utils import Choices


class Persona(models.Model):
    nombres = models.CharField(max_length=100, blank=True, null=True)
    apellidos = models.CharField(max_length=100, blank=True, null=True)
    razon_social = models.CharField(max_length=100, blank=True, null=True)

    dni = models.CharField(max_length=10, blank=True, null=True, unique=True)
    cuit = models.CharField(max_length=15, blank=True, null=True)

    domicilio = models.ForeignKey("Domicilio")
    telefono = models.CharField(max_length=20)

    def __unicode__(self):
        return "%s, %s (%s)" % (self.apellidos, self.nombres, self.dni)


class Titulo(models.Model):
    nombre = models.CharField(max_length=100)

    def __unicode__(self):
        return self.nombre


class Profesional(models.Model):
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    dni = models.CharField('DNI',
                           max_length=10,
                           blank=True,
                           null=True)
    titulo = models.ForeignKey(Titulo, blank=True, null=True)
    matricula = models.CharField('Número Matrícula',
                                 max_length=50,
                                 blank=True,
                                 null=True)
    telefono = models.CharField('Teléfono',
                                max_length=20,
                                blank=True,
                                null=True)

    def __unicode__(self):
        return "%s, %s" % (self.apellidos, self.nombres)

    class Meta:
        verbose_name_plural = 'Profesionales'


class Domicilio(models.Model):
    direccion = models.CharField(max_length=80)
    descripcion = models.TextField(blank=True, null=True)
    localidad = models.ForeignKey('Localidad')

    def __unicode__(self):
        return self.direccion


class Localidad(models.Model):
    nombre = models.CharField(max_length=50)
    codigo_postal = models.CharField(max_length=15)

    def __unicode__(self):
        return "%s (%s)" % (self.nombre, self.codigo_postal)

    class Meta:
        verbose_name_plural = 'Localidades'
