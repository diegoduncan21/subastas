# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subastas', '0005_auto_20150629_2009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rodado',
            name='lote',
            field=models.ForeignKey(related_name='bienes', blank=True, to='subastas.Lote', null=True),
            preserve_default=True,
        ),
    ]
