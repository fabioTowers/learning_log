from django.contrib import admin

# importando Topic e Entry
from learning_logs.models import Topic, Entry

# Register your models here.
# Aqui ficam os modelos (models.py) que são administrados no site de administração

#Administre Topic e Entry por meio do site de administração:
admin.site.register(Topic)
admin.site.register(Entry)
