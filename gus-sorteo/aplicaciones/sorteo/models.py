from django.db import models
from uuid import uuid4


class Codigo(models.Model):
    id = models.AutoField(primary_key=True)
    codigo = models.CharField(max_length=4)
    asignado = models.BooleanField(default=0)

    def __str__(self) -> str:
        return self.codigo


class Participante(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    codigo = models.ForeignKey(Codigo, blank=False, null=False, on_delete=models.CASCADE)
    nombre_completo = models.CharField(max_length=50)
    correo_electronico = models.EmailField(max_length=50)
    celular = models.CharField(max_length=8)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return "{} | {}".format(self.nombre_completo, self.fecha_registro)
