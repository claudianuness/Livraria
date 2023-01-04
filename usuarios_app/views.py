from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from .forms import UsuarioForm
from django.urls import reverse_lazy


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
