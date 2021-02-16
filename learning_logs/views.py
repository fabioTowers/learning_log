from django.shortcuts import render

# Importando o modelo de dados necessário
from .models import Topic

# Create your views here.
#Em urls.py definimos a view index, que está definida abaixo
# o request será passado a essa função, que por sua vez chama a 
# função render() que recebe o request e uma página que deve ser retornada
def index(request):
    """A página inicial de Learning Log"""
    return render(request, 'learning_logs/index.html')

def topics(request):
    """Mostra todos os assuntos."""
    # Consulta ao banco de dados, solicitando os objetos Topic
    #ordenados pelo atributo 'date_added', o queryset de 
    #resposta é armazenado em topics
    topics = Topic.objects.order_by('date_added')

    # Abaixo temos o contexto: as chaves são os nomes que 
    #serão usados no template para acessar, e os valores são 
    #os dados que vamos enviar 
    context = {'topics': topics}

    # Passamos ao método render() o request, o caminho do 
    #template, e os dados a serem exibidos (context)
    return render(request, 'learning_logs/topics.html', context)

#O segundo parâmetro é o valor recebido no mapeamento de URL's com o assunto
# que será renderizado na página
def topic(request, topic_id):
    """Mostra um único assunto e todas as suas entradas."""
    
    #Obtendo o assunto do banco de dados (registro onde o id corresponde)
    topic = Topic.objects.get(id=topic_id)

    # recuperamos as entradas associadas ao assunto ordenados de acordo com a 
    #data que foram adicionados. O menos indica para ordenar na ordem inversa
    #isso faz com que as entradas mais recentes sejam exibidas antes.
    entries = topic.entry_set.order_by('-date_added')

    # Os dados recuperados são associados ao dicionário context
    context = {'topic': topic, 'entries': entries}

    # O dicionários é enviado ao template topic.html
    return render(request, 'learning_logs/topic.html', context)
