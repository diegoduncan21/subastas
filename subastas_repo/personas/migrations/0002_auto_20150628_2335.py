# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profesional',
            name='dni',
            field=models.CharField(max_length=10, null=True, verbose_name=b'DNI', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='profesional',
            name='matricula',
            field=models.CharField(max_length=50, null=True, verbose_name=b'N\xc3\xbamero Matr\xc3\xadcula', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='profesional',
            name='telefono',
            field=models.CharField(max_length=20, null=True, verbose_name=b'Tel\xc3\xa9fono', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='profesional',
            name='titulo',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name=b'Titulo', choices=[(b'abogado', b'Abogado'), (b'escribano', b'Escribano'), (b'martillero', b'Martillero')]),
            preserve_default=True,
        ),
    ]
