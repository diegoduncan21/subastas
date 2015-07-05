# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subastas', '0003_auto_20150628_2335'),
    ]

    operations = [
        migrations.AddField(
            model_name='lote',
            name='grupo',
            field=models.ForeignKey(related_name='lotes', default=2, to='subastas.Grupo'),
            preserve_default=False,
        ),
    ]
