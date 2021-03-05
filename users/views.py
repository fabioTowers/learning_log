from django.shortcuts import render

from django.http import HttpResponseRedirect

# A função reverse() determina o URL a partir de um padrão de URL
#nomeado. O django vai gerar um URL quando a págin for solicitada
#from django.core.urlresolvers import reverse
from django.urls import reverse

# Para importa a função logout()
from django.contrib.auth import logout

# Create your views here.

def logout_view(request):
    """Faz logout do usuário."""
    logout(request)
    # Redireciona para a página inicial
    return HttpResponseRedirect(reverse('learning_logs:index'))
