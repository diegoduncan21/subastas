# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'permissions': (('administrador', 'Administrador'), ('acreditador', 'Acreditador'), ('actero', 'Actero'))},
        ),
    ]
