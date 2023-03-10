from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Carrinho


class UsuarioForm(UserCreationForm):
    email = forms.EmailField(max_length=100)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class CarrinhoForm(ModelForm):
    class Meta:
        model = Carrinho
        fields = ["produto", "quantidade"]
