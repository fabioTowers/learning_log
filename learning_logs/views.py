from django.shortcuts import render

# Importando os modelos de dados necessário
from .models import Topic, Entry

# Essa classe vai redirecionar o leitor de volta a página topics
#após ele ter submentido um assunto
from django.http import HttpResponseRedirect, Http404

# A função reverse() determina o URL a partir de um padrão de URL
#nomeado. O django vai gerar um URL quando a págin for solicitada
#from django.core.urlresolvers import reverse
from django.urls import reverse

# Importando TopicForm e EntryForm, que são os formulários criados em forms.py
from .forms import TopicForm, EntryForm

# Importando a função login_required()
from django.contrib.auth.decorators import login_required

# Create your views here.
#Em urls.py definimos a view index, que está definida abaixo
# o request será passado a essa função, que por sua vez chama a 
# função render() que recebe o request e uma página que deve ser retornada
def index(request):
    """A página inicial de Learning Log"""
    return render(request, 'learning_logs/index.html')

# A anotação @login_required restringe a execução dessa função
#apenas a usuários logados, com a anotação python sabe que deve
#executar login_required() antes de topics()
@login_required
def topics(request):
    """Mostra todos os assuntos."""
    # Consulta ao banco de dados, solicitando os objetos Topic
    #ordenados pelo atributo 'date_added', o queryset de 
    #resposta é armazenado em topics
    #filter faz com que sejam retornados apenas assuntos relacionados ao usuário logado
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')

    # Abaixo temos o contexto: as chaves são os nomes que 
    #serão usados no template para acessar, e os valores são 
    #os dados que vamos enviar 
    context = {'topics': topics}

    # Passamos ao método render() o request, o caminho do 
    #template, e os dados a serem exibidos (context)
    return render(request, 'learning_logs/topics.html', context)

#O segundo parâmetro é o valor recebido no mapeamento de URL's com o assunto
# que será renderizado na página
@login_required
def topic(request, topic_id):
    """Mostra um único assunto e todas as suas entradas."""
    
    #Obtendo o assunto do banco de dados (registro onde o id corresponde)
    topic = Topic.objects.get(id=topic_id)

    # Garante que o assunto pertence ao usuário atual
    if topic.owner != request.user:
        raise Http404

    # recuperamos as entradas associadas ao assunto ordenados de acordo com a 
    #data que foram adicionados. O menos indica para ordenar na ordem inversa
    #isso faz com que as entradas mais recentes sejam exibidas antes.
    entries = topic.entry_set.order_by('-date_added')

    # Os dados recuperados são associados ao dicionário context
    context = {'topic': topic, 'entries': entries}

    # O dicionários é enviado ao template topic.html
    return render(request, 'learning_logs/topic.html', context)

# Tratamento da requisição ao solicitar a inserção de um novo assunto
@login_required
def new_topic(request):
    """Adiciona um novo assunto."""
    if request.method != 'POST':
        # Nenhum dados submetido: cria um formulario em branco
        form = TopicForm()
    else:
        # Dados do POST submetidos: processa esses dados
        #os dados que o usuário colocou no formulário estão em request.POST
        form = TopicForm(request.POST)
        # is_valid() verifica se as informações são válidas e se todos os 
        #campos obrigatórios foram preenchidos (por padrão, todos são
        #obrigatórios), verifica se os tipos de dados correspondentes foram
        #colocados em cada campo, foi especificado também (em models.py) que
        #o tamanho máximo é 200 caracteres, essa função também verifica isso
        if form.is_valid():
            # save() salva os dados do formulário no banco de dados
            form.save()
            # Redireciona o usuário para a página de tópicos
            return HttpResponseRedirect(reverse('learning_logs:topics'))

    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)

@login_required
def new_entry(request, topic_id):
    """Acrescenta uma nova entrada para um assunto em particular."""
    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        # Nenhum dado submetido; cria um formulário em branco
        form = EntryForm()
    else:
        # Dados de POST submetidos; processa os dados
        form = EntryForm(data=request.POST)
        # Verifica se o formulário foi corretamente preenchido
        if form.is_valid():
            # Criar um novo objeto nem_entry sem salvar no banco por enquanto
            new_entry = form.save(commit=False)
            # Definindo o atributo topic
            new_entry.topic = topic
            # Efetivamente salva no banco de dados com o assunto correto associado
            new_entry.save()
            # Redirecionar o usuário para a página do assunto
            #A função reverse exige dois argumentos:
            # - Nome do padrão de URL para o qual queremos gerar um URL;
            # - Uma lista de argumentos contendo qualquer argumento que deva ser incluída na URL
            return HttpResponseRedirect(reverse('learning_logs:topic', args=[topic_id]))

    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)

# Recebe as requisições da página de edição de uma entrada
@login_required
def edit_entry(request, entry_id):
    """Edita uma nova entrada existente."""
    # Pega o objeto da entrada que o usuário quer editar e o assunto associado
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic

    # Restrição que garante que apenas o usuário proprietário dessa entrada possa editá-la
    if topic.owner != request.user:
        raise Http404

    if request.method != 'POST':
        #Requisição inicial; preenche previamente o formulário com a entrada atual
        # criada uma instância de EntryForm com o argumento instance
        # dessa forma, quando o usuário solocitar editar uma entrada ele vai ver a 
        #caixa de texto preenchida com seu valor atual
        form = EntryForm(instance=entry)
    else:
        # Dados de POST submetidos; processa os dados
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learning_logs:topic', args=[topic.id]))

    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)
