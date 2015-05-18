# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subastas', '0003_auto_20150517_2307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rodado',
            name='modelo',
            field=models.CharField(max_length=15),
            preserve_default=True,
        ),
    ]
