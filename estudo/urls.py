from django.urls import path
from . import views

urlpatterns = [
    path('ver_produtos/', views.ver_produtos, name='ver_produtos'),
    path('catalogo/', views.catalogo, name='catalogo')
]
