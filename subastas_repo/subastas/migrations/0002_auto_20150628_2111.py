# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subastas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rodado',
            name='lote',
            field=models.ForeignKey(blank=True, to='subastas.Lote', null=True),
            preserve_default=True,
        ),
    ]
