import re
from django import forms

from .models import Listing


class ListingForm(forms.ModelForm):
    image = forms.ImageField()

    class Meta:
        model = Listing
        fields = {'brand', 'model', 'vin', 'mileage',
                  'color', 'description', 'engine', 'transmisson', 'image'}
