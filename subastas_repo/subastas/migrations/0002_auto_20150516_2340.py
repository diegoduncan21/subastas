# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subastas', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rodado',
            name='caracteristicas',
        ),
        migrations.DeleteModel(
            name='Caracteristica',
        ),
        migrations.AddField(
            model_name='rodado',
            name='descripcion',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
