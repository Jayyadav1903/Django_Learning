from django import forms
from .models import biryani_variety

class BiryaniForm(forms.Form):
    biryani_variety = forms.ModelChoiceField(queryset=biryani_variety.objects.all(), label="Select Biryani Variety")  
    