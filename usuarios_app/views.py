from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from .forms import UsuarioForm, CarrinhoForm
from django.urls import reverse_lazy
from .models import Cliente, Carrinho , Shop


# Create your views here.
class CriarUsuario(CreateView):
    template_name = 'usuarios_app/form.html'
    form_class = UsuarioForm
    success_url = reverse_lazy('login')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['title'] = 'Create User'
        context['bootom'] = 'Register'
        return context


from django.shortcuts import render

# Create your views here.

def shopping_items_add(request):
    cliente = Cliente.objects.get(email=request.user.email)
    dados = {}
    form = CarrinhoForm(request.POST or None)

    if form.is_valid():
        form.instance.shop = Shop.objects.create(nome_cliente = cliente)
        form.save()

    dados["form"] = form
    
    return render(request, "primeira_app/carrinho_form.html", dados)

def cart_items(request, pk):
    template_name = 'cart_items.html'
    carts = Carrinho.objects.filter(shop=pk)

    qs = carts.values_list('price', 'quantity') or 0
    total = sum(map(lambda q: q[0] * q[1], qs))

    context = {'object_list': carts, 'total': total}
    return render(request, template_name, context)