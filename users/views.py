from django.shortcuts import render

from django.http import HttpResponseRedirect

# A função reverse() determina o URL a partir de um padrão de URL
#nomeado. O django vai gerar um URL quando a págin for solicitada
#from django.core.urlresolvers import reverse
from django.urls import reverse

# Para importa a função logout()
from django.contrib.auth import logout

from django.contrib.auth import login, logout, authenticate

# Importamos o fomulário default para cadastro de novos usuários
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def logout_view(request):
    """Faz logout do usuário."""
    logout(request)
    # Redireciona para a página inicial
    return HttpResponseRedirect(reverse('learning_logs:index'))

# A primeira requisição envia o formulário em branco
# A segunda requisição envia o formulário preenchido (POST)
def register(request):
    """Faz o cadastro de um novo usuário."""
    if request.method != 'POST':
        # Exibe o formulário de cadastro em branco
        #cria uma nova instância de UserCreationForm sem dados
        form = UserCreationForm()
    else:
        # Processa o formulário preenchido
        #cria uma instância de UserCreationForm com base nos dados preenchidos
        form = UserCreationForm( data=request.POST )
        #a função is_valid verifica:
        #o nome de usuário possui caracteres válidos?
        #as senhas digitadas são iguais?
        #os dados possuem algum código potenciamente malicioso?
        if form.is_valid():
            #save() salva no banco de dados o nome do usuário e o hash da senha
            new_user = form.save()
            # Faz login do usuário e o redireciona para a página inicial
            #o método authenticate recebe dois argumentos: nome do usuário e senha
            #ao se cadastrar o usuário escreve a senha duas vezes (confirmação), nesse caso usamos a senha 1 (password1)
            # o método retorna o objeto que representa o usuário autenticado
            authenticate_user = authenticate(username=new_user.username, password=request.POST['password1'])
            # passamos o usuário autenticado para login() que cria uma seção válida
            login(request, authenticate_user)
            #Usuário é redirecionado para a tela inicial
            return HttpResponseRedirect(reverse('learning_logs:index'))
    
    context = {'form': form}
    return render(request, 'users/register.html', context)
