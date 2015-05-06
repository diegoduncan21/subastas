# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0001_initial'),
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
            name='Caracteristica',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('marca', models.CharField(max_length=50)),
                ('modelo', models.CharField(max_length=50)),
                ('descripcion', models.TextField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Rodado',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('numero_inventario', models.IntegerField()),
                ('modelo', models.IntegerField()),
                ('chasis', models.CharField(max_length=15)),
                ('motor', models.CharField(max_length=10)),
                ('dominio', models.CharField(max_length=12)),
                ('precio_base', models.FloatField(default=0)),
                ('precio_venta', models.FloatField(default=0)),
                ('lote', models.IntegerField()),
                ('chatarra', models.BooleanField(default=False)),
                ('caracteristicas', models.ForeignKey(to='subastas.Caracteristica')),
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
                ('actas', models.ManyToManyField(to='subastas.Acta', null=True, blank=True)),
                ('bienes', models.ManyToManyField(to='subastas.Rodado')),
                ('domicilio', models.ForeignKey(to='personas.Domicilio')),
                ('personas', models.ManyToManyField(to='personas.Persona', null=True, blank=True)),
                ('profesionales', models.ManyToManyField(to='personas.Profesional')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='acta',
            name='bien_rodado',
            field=models.ForeignKey(to='subastas.Rodado'),
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
    ]
