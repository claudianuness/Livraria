from django.urls import path
from . import views

urlpatterns = [
    path("", views.home),
    path("listagem/", views.listagem, name="url_listagem"),
    path("form/", views.criar),
    path("delete/<int:pk>/", views.delete, name="url_delete"),
    path("novo/", views.criar, name="url_novo"),
    path('update/<int:pk>/', views.update, name='url_update'),
    path('buscar_livro/', views.buscar),
]
