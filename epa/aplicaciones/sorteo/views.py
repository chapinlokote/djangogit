from django.shortcuts import render, redirect, get_object_or_404
from pytz import timezone
from .models import Participantes
# Create your views here.

def home(request):
    return render(request, "index.html")

def agregarParticipantes(request):
    codigo=request.POST['txtCodigo']
    nombre=request.POST['txtNombre']
    correo=request.POST['txtCorreo']
    celular=request.POST['txtCelular']
    #fecha_actualizado=request.POST['txtFecha_a']
    #participantes = Participantes.objects.create(
    #codigo=codigo, nombre=nombre, correo=correo, celular=celular)
    codigo = Participantes.objects.get(codigo=codigo)
    #codigo = get_object_or_404(Participantes, codigo=codigo)

    codigo.nombre = nombre
    codigo.correo = correo
    codigo.celular = celular
    #codigo.fecha_actualizado = datetime.now()
    codigo.save()

    return render(request, "index.html")    