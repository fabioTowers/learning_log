"""learning_log URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
#Importando os módulos que administram os URL's
from django.contrib import admin
from django.urls import path, include

# A varíavel urlpatterns: conjuntos de URL's do projeto. Os URL's que podem ser
#requisitados a partir do site de administração
#note que há dois namespace's: users e learning_logs, isso é para distinguir o
#conjunto de URL's pertencentes a cada aplicação
urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls', namespace='users')),
    path('', include('learning_logs.urls', namespace='learning_logs'))
]
