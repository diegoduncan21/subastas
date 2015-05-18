# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subastas', '0002_auto_20150516_2340'),
    ]

    operations = [
        migrations.AddField(
            model_name='rodado',
            name='subastado',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='rodado',
            name='lote',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
