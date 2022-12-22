from django.shortcuts import render, redirect
from datetime import datetime
from .models import Livro
from .form import LivroForm


def home(request):
    dados = {"agora": datetime.now()}
    return render(request, "primeira_app/home.html", dados)


def listagem(request):
    dados = {"livros": Livro.objects.all()}
    return render(request, "primeira_app/listagem.html", dados)


def criar(request):
    dados = {}
    form = LivroForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect("url_listagem")

    dados["form"] = form
    return render(request, "primeira_app/form.html", dados)


def update(request, pk):
    dados = {}
    livro = Livro.objects.get(pk=pk)
    form = LivroForm(request.POST or None, instance=livro)

    if form.is_valid():
        form.save()
        return redirect("url_listagem")

    dados["form"] = form
    dados["livro"] = livro
    return render(request, "primeira_app/form.html", dados)


def delete(request, pk):
    livro = Livro.objects.get(pk=pk)
    livro.delete()
    return redirect("url_listagem")
