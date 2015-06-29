# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subastas', '0002_auto_20150628_2111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grupo',
            name='subasta',
            field=models.ForeignKey(related_name='grupos', blank=True, to='subastas.Subasta', null=True),
            preserve_default=True,
        ),
    ]
