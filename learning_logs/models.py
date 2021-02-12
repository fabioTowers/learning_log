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
    def __str__(self):
        """Devolve uma representação em string do modelo."""
        return self.text

# Mais um modelo de dado, mais uma tabela no banco
class Entry(models.Model):
    """Algo específico aprendido sobre um assunto."""
    # Possui uma chave-estrangeira, referenciando o conteúdo dessa tabela com Topic
    topic = models.ForeignKey(Topic, on_delete=models.DO_NOTHING)
    # Atributo do tipo TextField, que não precisa de limite de tamanho
    text = models.TextField(default="Nada aqui por enquanto...")
    # Atributo que adiciona etiqueta de tempo ao registro
    date_added = models.DateTimeField(auto_now_add=True)

    #Meta informação para o django: para se referir a mais de uma entrada o django usara entries
    # e não entrys (que seria o default)
    class Meta:
        verbose_name_plural = 'entries'
    
    # Quais informações devem ser mostradas quando entradas individuais forem referenciadas
    # A entrada pode ser longa, então definimos que exiba apenas os 50 primeiros caracteres da
    # string e com reticiências para deixar clara que foi cortado um trecho
    def __str__(self):
       """Devolve uma representação em string do modelo."""
       return self.text[:50] + "..."
