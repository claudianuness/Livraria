from django.urls import path
from django.contrib.auth import views as auth_views
from primeira_app import views
from .views import CriarUsuario

urlpatterns = [
    path("login/", auth_views.LoginView.as_view(
        template_name="usuarios_app/login.html",
    ), name="url_login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("registrar/", CriarUsuario.as_view(), name="registrar"),
    path("logout/", auth_views.LogoutView.as_view(), name="url_logout"),
    path("registrar/", CriarUsuario.as_view(), name="url_registrar"),
]

