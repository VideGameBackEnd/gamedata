# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gamedata', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='score',
            name='nombre',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='score',
            name='partido',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='score',
            name='score',
            field=models.IntegerField(default=0),
        ),
    ]
