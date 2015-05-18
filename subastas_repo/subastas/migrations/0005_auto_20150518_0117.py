# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subastas', '0004_auto_20150518_0111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rodado',
            name='chasis',
            field=models.CharField(max_length=50),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='rodado',
            name='dominio',
            field=models.CharField(max_length=50),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='rodado',
            name='modelo',
            field=models.CharField(max_length=50),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='rodado',
            name='motor',
            field=models.CharField(max_length=50),
            preserve_default=True,
        ),
    ]
