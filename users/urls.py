"""Define padrões de URL para a aplicação users"""

from django.conf.urls import url

# Importando a view de login default do Django
from django.contrib.auth.views import LoginView

from . import views

app_name = 'users'

urlpatterns = [
    # Página de login
    url(r'^login/$', LoginView.as_view(template_name='users/login.html'), name='login'),
]
