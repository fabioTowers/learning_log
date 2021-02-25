# Importando o módulo forms
from django import forms

# importando o modelo Topic que definimos e o modelo Entry
from .models import Topic, Entry


# Definimos a classe TopicForms quer herda de forms.modelForm
class TopicForm(forms.ModelForm):
    # A classe aninhada Meta, diz ao django para em qual modelo
    #o formulario deve se basear e quais seus campos
    class Meta:
        # O modelo se baseará em Topic (Template)
        model = Topic
        # Incluindo o campo Text
        fields = ['text']
        # Especifica ao django para não gerar um rótulo para o campo
        labels = {'text': ''}

# Essa classe herda de ModelForm
class EntryForm(forms.ModelForm):
    # Classe Meta aninhada que lista o modelo no qual ela está baseada
    #e o campo a ser incluído no formulário
    class Meta:
        model = Entry
        fields = ['text']
        # Rótulo vazio para text
        labels = {'text': ''}
        # Widget é um elemento de formulário HTML, com ele podemos 
        #sobrescrever atributos default de um elemento.
        # Nesse caso estamos definindo que text area terá 80 colunas 
        #ao invés das 40 padrão.
        widgets = {'text': forms.Textarea(attrs={'cols':80})}
