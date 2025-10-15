from django.urls import path
from . import views

urlpatterns = [
    path('jyud2.0/', views.ver_produtos, name='ver_produtos'),
    path('jyud/', views.catalogo, name='catalogo')
]
