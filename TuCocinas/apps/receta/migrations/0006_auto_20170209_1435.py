# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-02-09 19:35
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receta', '0005_remove_receta_calificacion_receta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receta',
            name='heart_like_receta',
            field=models.ManyToManyField(blank=True, related_name='heart_like_receta', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='receta',
            name='star_like_receta',
            field=models.ManyToManyField(blank=True, related_name='star_like_receta', to=settings.AUTH_USER_MODEL),
        ),
    ]
