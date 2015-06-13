# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subastas', '0006_auto_20150518_0134'),
    ]

    operations = [
        migrations.AddField(
            model_name='rodado',
            name='anio',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
