from django.urls import path
from carrinho_app import views

urlpatterns = [
    path("carrinho/", views.carrinho, name="url_carrinho"),

]