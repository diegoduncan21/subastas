# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subastas', '0006_auto_20150629_2047'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subasta',
            name='bienes',
        ),
    ]
