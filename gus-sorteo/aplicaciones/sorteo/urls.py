from django.urls import path
from aplicaciones.sorteo.views import index, registrar_participante

urlpatterns = [
    path('', index, name='index'),
    path('registrar_participante/', registrar_participante, name='registrar_participante')
]
