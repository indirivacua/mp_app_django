from django.urls import path
from . import views

urlpatterns = [
    path('', views.producto_lista, name='producto_lista'),
    path('agregar/', views.producto_agregar, name='producto_agregar'),
    path('<int:pk>/', views.producto_detalle, name='producto_detalle'),
    path('payment/success/', views.payment_success, name='payment_success'),
    path('payment/failure/', views.payment_failure, name='payment_failure'),
    path('payment/pending/', views.payment_pending, name='payment_pending'),
]
