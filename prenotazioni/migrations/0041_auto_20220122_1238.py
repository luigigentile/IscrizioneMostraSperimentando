# Generated by Django 3.0.7 on 2022-01-22 12:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('prenotazioni', '0040_movimentiprenotazione_orario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movimentiprenotazione',
            name='orario',
        ),
        migrations.RemoveField(
            model_name='movimentiprenotazione',
            name='orario_turno',
        ),
        migrations.RemoveField(
            model_name='movimentiprenotazione',
            name='settore',
        ),
    ]
