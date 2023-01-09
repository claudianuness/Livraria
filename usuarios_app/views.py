from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.shortcuts import render

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
