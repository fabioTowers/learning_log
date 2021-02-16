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

    # Página de detalhes para um único assunto
    #O primeiro parâmetro é um regex:
    #r interprete a string como pura
    #/(?P<topic_id>\d+)/ entre as barras teremos um inteiro e armazena o valor em topic_id
    #\d+ indica qualquer quantidade de dígitos que apareça entre as barras
    #Quando um endereço de requisição corresponde so padrão, será chamada a função de view topic()
    #com o argumento topic_id
    url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
]
