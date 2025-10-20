from django.urls import path
from . import views

urlpatterns = [
    path('inicio/', views.inicio, name='inicio'),       
    path('menu/', views.menu, name='menu'),      
    path('carrito/', views.carrito, name='carrito'),  
]
