# Generated by Django 5.1.7 on 2025-05-29 01:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reserva', '0002_reserva_estado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='estado',
            field=models.CharField(default='Confirmado', max_length=100),
        ),
    ]
