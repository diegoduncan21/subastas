# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subastas', '0009_auto_20150705_0100'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='grupo',
            unique_together=set([('subasta', 'numero')]),
        ),
    ]
