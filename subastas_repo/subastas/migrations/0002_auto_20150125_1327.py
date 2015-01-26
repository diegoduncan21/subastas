# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subastas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actas',
            name='descripcion',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='subasta',
            name='actas',
            field=models.ManyToManyField(to='subastas.Actas', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='subasta',
            name='personas',
            field=models.ManyToManyField(to='personas.Persona', null=True, blank=True),
            preserve_default=True,
        ),
    ]
