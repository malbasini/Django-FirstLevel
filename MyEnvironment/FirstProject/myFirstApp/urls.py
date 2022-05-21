from django.urls import path
#Importiamo la view
from myFirstApp import views as primaAppViews
urlpatterns = [
    path('',primaAppViews.homepage,name='home')
]
