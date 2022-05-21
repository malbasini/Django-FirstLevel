"""FirstProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path,include
#Importiamo la view
from myFirstApp import views as primaAppViews
urlpatterns = [
    path('admin/', admin.site.urls),
    #path('homepage/',primaAppViews.homepage,name='home')
    #Se vogliamo andare direttamente nella homepage specifichiamo questo percorso
    #path('',primaAppViews.homepage,name='home')
    #possiamo anche includere un file urls della nostra applicazione, dopo averlo creato
    path('', include('myFirstApp.urls'))
]
