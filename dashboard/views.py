from django.http.response import Http404, JsonResponse
from django.views.generic import View
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect 
from . import my_folium
from . import forms
from .models import PaddyAreaInfo

# Create your views here.
def index(request):
    map_ = my_folium.getMap()
    # map_ = my_folium.getMap(ee = True)

    # instantiate the form to create new paddy
    form = forms.PaddyAreaInfoForm()

    # query all paddy areas from db
    paddy_areas = PaddyAreaInfo.objects.all()
    
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

def test_info(request):
    form = forms.PaddyAreaInfoForm()

    return render(request, 'dashboard/test_info.html', {'form': form})

def say_hello(request):
    return render(request, 'dashboard/hello.html', {'name': 'Mosh'})

class DeletePaddyArea(View):
    def  get(self, request):
        id1 = request.GET.get('id', None)
        PaddyAreaInfo.objects.get(id=id1).delete()
        data = {
            'deleted': True
        }
        return JsonResponse(data)





 