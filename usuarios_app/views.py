from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.shortcuts import render
from .forms import EnderecoForm
import requests

from mysite.settings import LOGIN_REDIRECT_URL
from .forms import UsuarioForm, CarrinhoForm
from .models import Cliente, Carrinho, Shop


class CriarUsuario(CreateView):
    template_name = 'usuarios_app/form.html'
    form_class = UsuarioForm
    success_url = reverse_lazy('login')

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return HttpResponseRedirect(LOGIN_REDIRECT_URL)
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['title'] = 'Create User'
        context['bootom'] = 'Register'
        return context


def shopping_items_add(request):
    cliente = Cliente.objects.get(email=request.user.email)
    dados = {}
    form = CarrinhoForm(request.POST or None)

    if form.is_valid():
        form.instance.shop = Shop.objects.create(nome_cliente = cliente)
        form.save()

    dados["form"] = form

    return render(request, "livraria_app/form.html", dados)


def cart_items(request, pk):
    template_name = 'cart_items.html'
    carts = Carrinho.objects.filter(shop=pk)

    qs = carts.values_list('price', 'quantity') or 0
    total = sum(map(lambda q: q[0] * q[1], qs))

    context = {'object_list': carts, 'total': total}
    return render(request, template_name, context)


def cadastrar_endereco(request):
    if 'busca-cep' in request.POST:
        cep = request.POST['busca-cep']
        cep = cep.replace("-", "").replace(".", "").replace(" ", "").replace(",", "")
        if len(cep) == 8:
            link = f'https://viacep.com.br/ws/{cep}/json/'
            requisicao = requests.get(link)
            endereco = requisicao.json()
            print(endereco)
            dados = {"cep": endereco}
            return render(request, "usuarios_app/endereco_cadastro.html", dados)
        else:
            dados = {"cep": "CEP Inválido!"}
            return render(request, "usuarios_app/endereco_cadastro.html", dados)
    elif 'cep' in request.POST:
        EnderecoForm.fields['cep'] = 50720590
        form.nome
    else:
        return render(request, "usuarios_app/endereco_cadastro.html", {})

