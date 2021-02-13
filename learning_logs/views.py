from django.shortcuts import render

# Create your views here.
#Em urls.py definimos a view index, que está definida abaixo
# o request será passado a essa função, que por sua vez chama a 
# função render() que recebe o request e uma página que deve ser retornada
def index(request):
    """A página inicial de Learning Log"""
    return render(request, 'learning_logs/index.html')
