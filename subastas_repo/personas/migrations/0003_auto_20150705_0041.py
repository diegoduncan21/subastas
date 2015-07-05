# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0002_auto_20150628_2335'),
    ]

    operations = [
        migrations.CreateModel(
            name='Titulo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='profesional',
            name='titulo',
            field=models.ForeignKey(blank=True, to='personas.Titulo', null=True),
            preserve_default=True,
        ),
    ]
