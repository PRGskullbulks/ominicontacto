# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2019-07-31 13:02
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('configuracion_telefonia_app', '0007_destino_entrante_keys'),
    ]

    operations = [
        migrations.CreateModel(
            name='DestinoPersonalizado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, unique=True, validators=[django.core.validators.RegexValidator('^[\\w]+$')], verbose_name='Nombre')),
                ('custom_destination', models.CharField(max_length=50, unique=True, validators=[django.core.validators.RegexValidator('^(\\w+,\\w+,\\w+|\\w+,\\w+|\\w+)$')], verbose_name='Localizaci\xf3n destino')),
            ],
        ),
        migrations.AlterField(
            model_name='destinoentrante',
            name='tipo',
            field=models.PositiveIntegerField(choices=[(1, 'Campa\xf1a entrante'), (2, 'Validaci\xf3n de fecha/hora'), (3, 'IVR'), (5, 'HangUp'), (9, 'Identificador cliente'), (7, 'Destino personalizado')]),
        ),
    ]
