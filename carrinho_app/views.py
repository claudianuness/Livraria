from django.shortcuts import render
from livraria_app.models import Livro
def carrinho(request):
    dados = {"livros": Livro.objects.all()}
    return render(request, "carrinho_app/carrinho.html", dados)