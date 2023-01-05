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
<<<<<<< Updated upstream
=======



def buscar_no_google_books(search: str) -> dict:
    params = {
        "key": GOOGLE_API_KEY,
        "q": f"isbn:{search}"
    }

    r = requests.get(f"{GOOGLE_BOOKS_URL}/volumes/", params=params)
    r_json = r.json()

    return r_json.get("items")


def buscar(request):
    form = BuscarForm(request.POST or None)

    resultado = None

    if form.is_valid():
        print(form.cleaned_data["isbn"])
        resultado = buscar_no_google_books(form.cleaned_data["isbn"])
        print(resultado)

        #<pre class="mt-3"><code>{{ resultado_titulo | pprint }}</code></pre>

        if resultado:
            #resultado_titulo = resultado[0]["volumeInfo"]["title"]
            resultado_titulo = form

            #a = Livro()
            #a.titulo = resultado[0]["volumeInfo"]["title"]

            #a.save()



    contexto = {
        "form": form,
        "resultado": resultado,
        "resultado_titulo": resultado_titulo,
    }

    return render(request, "meu_app/buscar_livro.html", contexto)

>>>>>>> Stashed changes
