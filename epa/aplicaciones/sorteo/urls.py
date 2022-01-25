from django.urls import path
from . import views

urlpatterns = [
    path('', views.home ),
    path('agregarParticipantes/', views.agregarParticipantes),
]