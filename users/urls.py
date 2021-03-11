"""Define padrões de URL para a aplicação users"""

from django.conf.urls import url

# Importando a view de login default do Django
from django.contrib.auth.views import LoginView

from . import views

app_name = 'users'

urlpatterns = [
    # Página de login
    url(r'^login/$', LoginView.as_view(template_name='users/login.html'), name='login'),
    # Página de logout:
    #Esse padrão de URL envia a requisição para logout_view()
    url(r'^logout/$', views.logout_view, name='logout'),
    #Página de cadastro:
    #corresponde ao padrão http://localhost:8000/users/register/
    #envia as requisições para register() na view
    url(r'^register/$', views.register, name='register'),
]
