# Generated by Django 5.1.2 on 2024-11-01 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='imagen',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]