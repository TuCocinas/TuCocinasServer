# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-02-17 23:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receta', '0012_auto_20170217_1850'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receta',
            name='tiempo_preparacion_receta',
            field=models.CharField(max_length=7),
        ),
    ]