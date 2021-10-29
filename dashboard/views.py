from django.shortcuts import render
from django.http import HttpResponse
from . import my_folium

def calculate():
    x=1
    y=2
    return x

# Create your views here.
def index(request):
    map_ = my_folium.getMap()
    # map_ = my_folium.getMap(ee = True)

    data = {
        'map': map_,
    }

    return render(request, 'dashboard/index.html', data)
    # return render(request, 'dashboard/index.html')

def say_hello(request):
    x = calculate()
    return render(request, 'dashboard/hello.html', {'name': 'Mosh'})


 