from django.urls import path
from .views import lista_libros, lista_usuarios, lista_prestamos

urlpatterns = [
    path('api/libros/', lista_libros, name='libros'),
    path('api/usuarios/', lista_usuarios, name='usuarios'),
    path('api/prestamos/', lista_prestamos, name='prestamos'),
]