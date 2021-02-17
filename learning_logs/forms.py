# Importando o módulo forms
from django import forms

# importando o modelo Topic que definimos
from .models import Topic

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
