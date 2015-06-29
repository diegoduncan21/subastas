# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Acta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.TextField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Grupo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('numero', models.IntegerField()),
                ('subastado', models.BooleanField(default=False)),
                ('martillero', models.ForeignKey(to='personas.Profesional')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Lote',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('numero', models.IntegerField()),
                ('subastado', models.BooleanField(default=False)),
                ('chatarra', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Rodado',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('numero_inventario', models.IntegerField(unique=True)),
                ('descripcion', models.TextField(null=True, blank=True)),
                ('modelo', models.CharField(max_length=50)),
                ('chasis', models.CharField(max_length=50)),
                ('motor', models.CharField(max_length=50)),
                ('dominio', models.CharField(max_length=50)),
                ('marca', models.CharField(max_length=100)),
                ('anio', models.IntegerField(null=True, verbose_name=b'A\xc3\xb1o', blank=True)),
                ('precio_base', models.FloatField(default=0)),
                ('precio_venta', models.FloatField(default=0)),
                ('subastado', models.BooleanField(default=False)),
                ('lote', models.ForeignKey(to='subastas.Lote')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Subasta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('numero', models.IntegerField()),
                ('fecha_hora', models.DateTimeField()),
                ('cerrado_el', models.DateTimeField(null=True, blank=True)),
                ('decreto', models.CharField(max_length=10)),
                ('bienes', models.ManyToManyField(to='subastas.Rodado')),
                ('domicilio', models.ForeignKey(to='personas.Domicilio')),
                ('personas', models.ManyToManyField(to='personas.Persona', null=True, blank=True)),
                ('profesionales', models.ManyToManyField(to='personas.Profesional')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tipo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='rodado',
            name='tipo',
            field=models.ForeignKey(to='subastas.Tipo'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='grupo',
            name='subasta',
            field=models.ForeignKey(to='subastas.Subasta'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='acta',
            name='lote',
            field=models.OneToOneField(to='subastas.Lote'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='acta',
            name='persona',
            field=models.ForeignKey(to='personas.Persona'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='acta',
            name='profesionales',
            field=models.ManyToManyField(to='personas.Profesional'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='acta',
            name='subasta',
            field=models.ForeignKey(related_name='actas', to='subastas.Subasta'),
            preserve_default=True,
        ),
    ]
