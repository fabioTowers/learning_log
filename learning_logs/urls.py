# DEFINE PADRÕES DE URL's PARA learning_logs

# Função para mapear as URL's às views
from django.conf.urls import url

# Importar as views que estão no mesmo diretório
from . import views

# Variável que lista as páginas que podem
urlpatterns = [
    # Página Inicial
    path('', views.index, name='index'),
]
