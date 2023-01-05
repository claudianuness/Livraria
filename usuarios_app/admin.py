from django.contrib import admin
from .models import Carrinho, Cliente, Livro, Autor


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    ...


@admin.register(Carrinho)
class CarrinhoAdmin(admin.ModelAdmin):
    ...


@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
    ...


@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    ...
