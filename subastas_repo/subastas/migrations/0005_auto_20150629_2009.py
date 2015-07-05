# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subastas', '0004_lote_grupo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lote',
            name='grupo',
            field=models.ForeignKey(related_name='lotes', blank=True, to='subastas.Grupo', null=True),
            preserve_default=True,
        ),
    ]
