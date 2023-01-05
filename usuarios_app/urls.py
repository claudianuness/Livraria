from django.contrib.auth import views as auth_views
from django.urls import path

from .views import CriarUsuario, shopping_items_add

login_view = auth_views.LoginView.as_view(
    template_name="usuarios_app/login.html",
    redirect_authenticated_user=True,
)

urlpatterns = [
    path("login/", login_view, name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="url_logout"),
    path("registrar/", CriarUsuario.as_view(), name="url_registrar"),
    path("carrinho/", shopping_items_add, name="carrinho"),
]
