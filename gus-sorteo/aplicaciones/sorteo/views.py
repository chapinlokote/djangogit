from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from .models import Codigo, Participante
import json


def index(request):
    return render(request, "index.html")


@require_http_methods(["POST"])
@csrf_exempt
def registrar_participante(request):
    json_data = json.loads(request.body)

    codigo = str(json_data['codigo'])
    codigos_validos_encontrados = list(Codigo.objects.filter(codigo=codigo, asignado=False).values())

    if (len(codigos_validos_encontrados) > 0):
        objeto_codigo = Codigo.objects.get(codigo=codigo)
        objeto_codigo.asignado = True
        objeto_codigo.save()

        Participante.objects.create(
            codigo=objeto_codigo,
            nombre_completo=json_data['nombreCompleto'],
            correo_electronico=json_data['correo'],
            celular=json_data['celular']
        )
        datos = {'mensaje': "EXITO"}
    else:
        datos = {'mensaje': "CODIGONOVALIDO"}

    return JsonResponse(datos)
