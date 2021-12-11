
from django import forms
from . import models
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field

class NewPaddyAreaInfoForm(forms.Form):
    area_name = forms.CharField(label = "Area Name", max_length = 225, required=True)
    start_date = forms.DateTimeField(label = "Strat Date(DD/MM/YYYY)", required=True)
    longitude = forms.DecimalField(label = "longitude (Min -180, Max 180)", max_digits = 9, decimal_places = 6, required=True)
    latitude = forms.DecimalField(label = "Latitude (Min 0, Max 90)", max_digits = 9, decimal_places = 6, required=True)

class PaddyAreaInfoForm(forms.ModelForm):

    class Meta:
        model = models.PaddyAreaInfo
        fields = '__all__'

        labels = {
            'area_name': ('Area Name'),
            'start_date': ('Start Date(DD/MM/YYYY)'),
            'longitude': ('longitude (Min -180, Max 180)'),
            'latitude': ('Latitude (Min 0, Max 90)'),
        }