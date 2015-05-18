# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subastas', '0005_auto_20150518_0117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rodado',
            name='numero_inventario',
            field=models.IntegerField(unique=True),
            preserve_default=True,
        ),
    ]
