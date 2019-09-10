from .models import Location
from django import forms

class LocationModelForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = [
            'name'
        ]
        labels = {
            "name" : "Location Name "

        }