# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2019-06-18 20:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ominicontacto_app', '0028_grupo_verbose'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='duraciondellamada',
            name='agente',
        ),
        migrations.DeleteModel(
            name='DuracionDeLlamada',
        ),
    ]
