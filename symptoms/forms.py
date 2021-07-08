from django import forms
from .models import Symptom

# create new symptom form from model 
class SymptomForm(forms.ModelForm):
    class Meta :
        model = Symptom
        fields = ('symptom_name',)
