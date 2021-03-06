from os import name
from django.urls import path
from django.urls import path
from . import views
from django.views.generic import TemplateView


app_name = 'dashboard'

urlpatterns = [
    path('', views.index), 
    path('index', views.index, name="index"), 
    path('paddy_area_details/<int:areaId>', views.paddy_area_details, name="paddy_area_details"), 
    path('delete',  views.DeletePaddyArea.as_view(), name='delete'),
    path('hello', views.say_hello), 
]