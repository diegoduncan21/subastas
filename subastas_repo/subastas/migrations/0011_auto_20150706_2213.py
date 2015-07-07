# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subastas', '0010_auto_20150706_2211'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='lote',
            unique_together=set([('grupo', 'numero')]),
        ),
    ]
