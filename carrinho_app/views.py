from django.shortcuts import render
from .forms import CarrinhoForm
from .models import Cliente, Carrinho, Shop

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