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

    # Padrão de URL para página de novos tópicos (assuntos)
    #a solicitação de view será enviada para a função new_topic
    url(r'^new_topic/$', views.new_topic, name='new_topic'),

    # Definição da URL da página para adicionar uma nova entrada em um assunto
    #note que essa página é 'filha' de uma página de assuntos
    #novamente adicionamos um valor numérico na variável topic_id
    #quando uma URL com esse padrão for requisitada, Django enviará a requisição
    #e o ID do assunto para a função de view new_entry()
    url(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry), name='new_entry'),
]
