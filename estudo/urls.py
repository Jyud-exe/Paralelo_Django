from django.urls import path
from . import views

urlpatterns = [
    path('jyud/', views.ver_produtos, name='ver_produtos'),
    path('jyud2.0/', views.catalogo, name='catalogo')
]
