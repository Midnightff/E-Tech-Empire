# Generated by Django 5.1.2 on 2024-11-12 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='role',
            field=models.CharField(choices=[('admin', 'Admin'), ('client', 'Client'), ('quest', 'Quest')], default='quest', max_length=10),
        ),
    ]
