# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-02-24 22:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receta', '0013_auto_20170217_1852'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receta',
            name='tiempo_preparacion_receta',
            field=models.CharField(max_length=20),
        ),
    ]