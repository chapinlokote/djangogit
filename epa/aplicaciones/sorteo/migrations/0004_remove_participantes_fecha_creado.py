# Generated by Django 3.1.3 on 2022-01-24 21:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sorteo', '0003_participantes_celular'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='participantes',
            name='fecha_creado',
        ),
    ]