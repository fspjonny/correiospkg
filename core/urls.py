from django.urls import include, path

urlpatterns = [
    path('', include('apps.encomendas.urls')),
]

handler404 = "apps.encomendas.views.handler404"