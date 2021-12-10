from os import name
from django.urls import path
from django.urls import path
from . import views
from django.views.generic import TemplateView


app_name = 'dashboard'

urlpatterns = [
    path('', views.index), 
    path('index', views.index, name="index"), 
    path('hello', views.say_hello), 
    # path('add_new_paddy_area', TemplateView.as_view(template_name="addmusic.html"), ), 
]