from django.forms import ModelForm
from .models import Specialbrew

class SpecialbrewForm(ModelForm):
    class Meta:
        model = Specialbrew
        fields = ['name', 'description', 'date', 'variety']