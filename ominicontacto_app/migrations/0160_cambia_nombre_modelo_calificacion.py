# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2018-02-05 21:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ominicontacto_app', '0159_supervisorprofile_borrado'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Calificacion',
            new_name='NombreCalificacion',
        ),
    ]