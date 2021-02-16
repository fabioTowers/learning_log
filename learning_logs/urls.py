# DEFINE PADRÕES DE URL's PARA learning_logs

# Função para mapear as URL's às views
from django.conf.urls import url

# Importar as views que estão no mesmo diretório
from . import views

app_name = 'learning_logs'

# Variável que lista as páginas que podem
urlpatterns = [
    # Página Inicial
    url(r'^$', views.index, name='index'),

    # Mostra todos os assuntos
    url(r'^topics/$', views.topics, name='topics'),
]
