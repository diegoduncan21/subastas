# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0002_auto_20150125_1327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profesional',
            name='titulo',
            field=models.CharField(blank=True, max_length=100, null=True, choices=[(b'abogado', b'Abogado'), (b'escribano', b'Escribano'), (b'martillero', b'Martillero')]),
            preserve_default=True,
        ),
    ]
