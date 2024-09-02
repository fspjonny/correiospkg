from django.urls import path

from .views import rastrear_encomenda, view_encomendas

urlpatterns = [
    path('', view_encomendas),
    path('rastrear', rastrear_encomenda, name='rastrear')
]
