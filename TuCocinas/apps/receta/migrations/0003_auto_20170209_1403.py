# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-02-09 19:03
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('receta', '0002_receta_slug_receta'),
    ]

    operations = [
        migrations.AddField(
            model_name='receta',
            name='heart_like_receta',
            field=models.ManyToManyField(related_name='heart_like_receta', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='receta',
            name='star_like_receta',
            field=models.ManyToManyField(related_name='star_like_receta', to=settings.AUTH_USER_MODEL),
        ),
    ]
