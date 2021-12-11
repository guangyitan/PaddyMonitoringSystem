from django.http.response import Http404, JsonResponse
from django.views.generic import View
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect 
from . import my_folium
from . import forms
from .models import PaddyAreaInfo

ee = False
# Create your views here.
def index(request):
    # query all paddy areas from db
    paddy_areas = PaddyAreaInfo.objects.all()
    
    # lat_lst = [2.226888, 2.226888, 2.226888]
    #     lng_lst = [102.166600, 102.166440, 102.166200]
    #     name_lst = ['aa', 'bb', 'cc']
    #     color_lst = ['green', 'orange', 'red']
    #     color_lst2 = ['purple', '#FFFF00', 'red']


    # map_ = my_folium.getMap(ee = ee)
    map_ = my_folium.getMap(ee = ee, paddy_area_info = paddy_areas)
    # map_ = my_folium.getMap(ee = True)

    # instantiate the form to create new paddy
    form = forms.PaddyAreaInfoForm()
    
    # bind all data into dictionary
    data = {
        'map': map_,
        'form': form,
        'paddy_areas': paddy_areas,
    }

    if request.method == 'POST':
        print("aa")
        # Create a form instance and populate it with data from the request (binding):
        form = forms.PaddyAreaInfoForm(request.POST)
        print(form.errors)
        # Check if the form is valid:
        if form.is_valid():
            print("form valid")
            print(form.cleaned_data)
            
            new_paddy_area = form.save() #true here to save the img to db in order to be retrieved

            # return render(request, 'dashboard/index.html')
            return redirect('index')

    return render(request, 'dashboard/index.html', data)

def paddy_area_details(request, areaId):

    if request.method == 'GET':
        map_ = my_folium.getMap(ee=ee)

        area_info = PaddyAreaInfo.objects.get(id = areaId)

        data = {
        'area_info': area_info,
        'map': map_,
    }
    return render(request, 'dashboard/paddy_area_details.html', data)

def test_info(request):
    form = forms.PaddyAreaInfoForm()

    return render(request, 'dashboard/test_info.html', {'form': form})

def say_hello(request):
    return render(request, 'dashboard/hello.html', {'name': 'Mosh'})

class DeletePaddyArea(View):
    def  get(self, request):
        id1 = request.GET.get('id', None)
        PaddyAreaInfo.objects.get(id = id1).delete()
        data = {
            'deleted': True
        }
        return JsonResponse(data)





 