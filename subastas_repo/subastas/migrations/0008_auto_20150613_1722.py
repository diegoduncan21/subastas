# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subastas', '0007_rodado_anio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rodado',
            name='anio',
            field=models.IntegerField(null=True, verbose_name=b'A\xc3\xb1o', blank=True),
            preserve_default=True,
        ),
    ]
