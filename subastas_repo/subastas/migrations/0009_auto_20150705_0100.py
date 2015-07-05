# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subastas', '0008_auto_20150704_2254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grupo',
            name='martillero',
            field=models.ForeignKey(blank=True, to='personas.Profesional', null=True),
            preserve_default=True,
        ),
    ]
