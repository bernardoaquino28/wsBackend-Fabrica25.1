from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_filmes, name='lista_filmes'),
    path('novo/', views.novo_filme, name='novo_filme'),
    path('editar/<pk>/', views.editar_filme, name='editar_filme'),
    path('excluir/<pk>/', views.excluir_filme, name='excluir_filme'),
    path('buscar/', views.buscar_filme_omdb, name='buscar_filme_omdb'),
]
