# Livraria
desenvolvimento web - backend - exemplo


# Dependencias 

criar ambiente virtual: python -m venv venv

django: python -m pip install django

crispy forms: python -m pip install django-crispy-forms

decouple: python -m pip install python-decouple

pagarme: python -m pip install django_pagarme (possível correção na importação do módulo: pip install 'git+https://github.com/pagarme/pagarme-python.git')


# Comandos

criar projeto: django-admin startproject nome-do-projeto

criar aplicativo: python manage.py startapp nome-do-app

criar usuário admin: python manage.py createsuperuser 
