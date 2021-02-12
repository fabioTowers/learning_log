from django.contrib import admin

# importando Topic
from learning_logs.models import Topic

# Register your models here.
# Aqui ficam os modelos (models.py) que são administrados no site de administração

#Administre Topic por meio do site de administração:
admin.site.register(Topic)
