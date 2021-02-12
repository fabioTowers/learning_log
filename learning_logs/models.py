from django.db import models

# Create your models here.

#Aqui ficam as classes

# Adicionamos um texto
# E para cada texto uma timestamp

# Classe Topic: Herda de Model (classe pai, define a funcionalidade básica de um modelo no django)
class Topic(models.Model):
    """Um assunto sobre o qual o usuário está aprendendo."""
    # atributo text: do tipo charfield, têm reservado no banco de dados um tamanho maxímo de 200 caracteres
    text = models.CharField(max_length=200)
    # atributo date_added: tipo DateTimeField (data e hora), auto_now_add armazena a hora e data atual
    date_added = models.DateTimeField(auto_now_add=True)

    # atributo default para exibir informações sobre um assunto
    # Método __str__() define uma representação simples de um modelo
    # Nesse caso devolve uma string armazenada em text
    def__str__(self):
        """Devolve uma representação em string do modelo."""
        return self.text
