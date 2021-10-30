from django import forms
from . import models
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field

class PaddyAreaInfoForm(forms.ModelForm):

    class Meta:
        model = models.PaddyAreaInfo
        fields = '__all__'

        labels = {
            'name': ('Area Name'),
            'start_date': ('Start Date(DD/MM/YYYY)'),
            'growth_calssification': ('Growth Classification'),
            'paddy_images': ('Paddy Images'),
        }