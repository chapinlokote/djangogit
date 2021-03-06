# Generated by Django 4.0.1 on 2022-01-27 23:19

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Codigo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('codigo', models.CharField(max_length=4)),
                ('asignado', models.BooleanField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Participante',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nombre_completo', models.CharField(max_length=50)),
                ('correo_electronico', models.EmailField(max_length=50)),
                ('celular', models.CharField(max_length=8)),
                ('fecha_registro', models.DateTimeField(auto_now_add=True)),
                ('codigo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sorteo.codigo')),
            ],
        ),
    ]
