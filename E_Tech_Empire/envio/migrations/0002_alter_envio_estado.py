# Generated by Django 5.1.2 on 2024-11-11 15:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('envio', '0001_initial'),
        ('estado', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='envio',
            name='estado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estado.estado'),
        ),
    ]
