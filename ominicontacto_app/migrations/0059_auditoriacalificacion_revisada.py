# Generated by Django 2.2.7 on 2020-06-30 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ominicontacto_app', '0058_valores_constance_redis_a_database'),
    ]

    operations = [
        migrations.AddField(
            model_name='auditoriacalificacion',
            name='revisada',
            field=models.BooleanField(default=False),
        ),
    ]