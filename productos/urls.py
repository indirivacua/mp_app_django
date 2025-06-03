from django.urls import path
from . import views

urlpatterns = [
    path('', views.producto_lista, name='producto_lista'),
    path('agregar/', views.producto_agregar, name='producto_agregar'),
    path('<int:pk>/', views.producto_detalle, name='producto_detalle'),
]
