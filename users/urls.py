"""Define padrões de URL para a aplicação users"""

from django.conf.urls import url

# Importando a view de login default do Django
from django.contrib.auth.views import login_required

from . import views

urlpatterns = [
    # Página de login
    url(r'^login/$', login, {'template_name': 'users/login.html'}, name='login'),
]
