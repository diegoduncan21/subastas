# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Domicilio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('direccion', models.CharField(max_length=80)),
                ('descripcion', models.TextField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Localidad',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50)),
                ('codigo_postal', models.CharField(max_length=15)),
            ],
            options={
                'verbose_name_plural': 'Localidades',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombres', models.CharField(max_length=100, null=True, blank=True)),
                ('apellidos', models.CharField(max_length=100, null=True, blank=True)),
                ('razon_social', models.CharField(max_length=100, null=True, blank=True)),
                ('dni', models.CharField(max_length=10, unique=True, null=True, blank=True)),
                ('cuit', models.CharField(max_length=15, null=True, blank=True)),
                ('telefono', models.CharField(max_length=20)),
                ('domicilio', models.ForeignKey(to='personas.Domicilio')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Profesional',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombres', models.CharField(max_length=100)),
                ('apellidos', models.CharField(max_length=100)),
                ('dni', models.CharField(max_length=10, null=True, blank=True)),
                ('titulo', models.CharField(blank=True, max_length=100, null=True, choices=[(b'abogado', b'Abogado'), (b'escribano', b'Escribano'), (b'martillero', b'Martillero')])),
                ('matricula', models.CharField(max_length=50, null=True, blank=True)),
                ('telefono', models.CharField(max_length=20, null=True, blank=True)),
            ],
            options={
                'verbose_name_plural': 'Profesionales',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='domicilio',
            name='localidad',
            field=models.ForeignKey(to='personas.Localidad'),
            preserve_default=True,
        ),
    ]
