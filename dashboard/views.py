from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect 
from . import my_folium
from . import forms


def calculate():
    x=1
    y=2
    return x

# Create your views here.
def index(request):
    # map_ = my_folium.getMap()
    map_ = my_folium.getMap(ee = True)

    form = forms.PaddyAreaInfoForm()

    data = {
        'map': map_,
        'form': form,
    }

    if request.method == 'POST':
        form = forms.PaddyAreaInfoForm(request.POST, request.FILES)
        if form.is_valid():
            
            return redirect('dashboard:index')

    return render(request, 'dashboard/index.html', data)
    # return render(request, 'dashboard/index.html')

# def add_new_paddy_area(request):
#     if request.method == 'POST':
#         form = forms.PaddyAreaInfoForm(request.POST, request.FILES)
#         if form.is_valid():
            
#             return redirect('dashboard:index')
#     else:
#         form = forms.PaddyAreaInfoForm()

#     return render(request, 'dashboard/index.html', {'form': form})

def say_hello(request):
    x = calculate()
    return render(request, 'dashboard/hello.html', {'name': 'Mosh'})





 