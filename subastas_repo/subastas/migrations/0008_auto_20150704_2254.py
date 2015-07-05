# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('subastas', '0007_remove_subasta_bienes'),
    ]

    operations = [
        migrations.AddField(
            model_name='subasta',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 4, 22, 54, 24, 258595), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='subasta',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 4, 22, 54, 31, 302189), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='subasta',
            name='user_updated',
            field=models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
    ]
