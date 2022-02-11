from django.http.response import Http404, JsonResponse
from django.views.generic import View
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect 
from . import my_folium
from . import forms
from .models import ImagePredictions, PaddyAreaInfo
from . import utils
import datetime
import os
from django.core.files import File  # you need this somewhere
import urllib.request

from . import predictModel

# ee = False
ee = True
# Create your views here.
def index(request):
    # query all paddy areas from db
    paddy_areas = PaddyAreaInfo.objects.all()

    # query latest predictions
    pred_list = []

    if paddy_areas.exists():
        map_ = my_folium.getMap(ee = ee, paddy_area_info = paddy_areas)
        for area_ in paddy_areas:
            pred_ = ImagePredictions.objects.filter(paddy_area_id = area_.id)

            # check if there is any image uploaded for prediciton
            if pred_:
                print(pred_)
                pred_ = pred_.latest('prediction_date').prediction
                pred_list.append(pred_)
            else:
                # prediciton = 6 if there is no prediction
                pred_list.append(6)
            

    # no paddy areas saved in db
    else:
        map_ = my_folium.getMap(ee = ee)

    # map_ = my_folium.getMap(ee = True)

    # instantiate the form to create new paddy
    form = forms.PaddyAreaInfoForm()
    
    paddy_areas = zip(paddy_areas, pred_list)
    # bind all data into dictionary
    data = {
        'map': map_,
        'form': form,
        'paddy_areas': paddy_areas,
    }
    print(pred_list)

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

    if request.method == 'POST':
        form = forms.ImagePredictionForm(request.POST, files=request.FILES)
        print(form.errors)

        if form.is_valid():
            print("form valid")
            print(form.cleaned_data)
            print(form.cleaned_data['paddy_area_id'])
            print(form.cleaned_data['image'])

            imgPredObj = ImagePredictions()
            imgPredObj.paddy_area_id = form.cleaned_data['paddy_area_id']
            imgPredObj.image = form.cleaned_data['image']
            # set TIME_ZONE = 'Etc/GMT+8' in settings.py
            imgPredObj.prediction_date = datetime.datetime.now()
            imgPredObj.prediction = 0
            imgPredObj.save()

            print(imgPredObj.id)
            img_ = ImagePredictions.objects.get(id = imgPredObj.id).image
            image_path = utils.get_image_directory(img_)
            print(image_path)

            # TODO: append model here
            predictModel.predictCustomImage(imgPredObj.id, image_path)

    area_info = PaddyAreaInfo.objects.filter(id = areaId)
    map_ = my_folium.getMap(ee=ee, paddy_area_info = area_info)
    predictions = ImagePredictions.objects.filter(paddy_area_id = areaId).order_by('-prediction_date')
    form = forms.ImagePredictionForm()

    data = {
        'area_info': area_info[0],
        'map': map_,
        'predictions': predictions,
        'form' : form,
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





 