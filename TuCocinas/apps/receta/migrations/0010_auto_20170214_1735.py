# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-02-14 22:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receta', '0009_recetapaso_foto_paso'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recetapaso',
            name='foto_paso',
            field=models.ImageField(blank=True, null=True, upload_to='img/recetas/pasos/'),
        ),
    ]