from django import forms
from .models import JuegoPC, JuegoNintendo, JuegoSony

class JuegoPCForm(forms.ModelForm):
    class Meta:
        model = JuegoPC
        fields = '__all__'

class JuegoNintendoForm(forms.ModelForm):
    class Meta:
        model = JuegoNintendo
        fields = '__all__'

class JuegoSonyForm(forms.ModelForm):
    class Meta:
        model = JuegoSony
        fields = '__all__'

class BusquedaForm(forms.Form):
    nombre = forms.CharField(label='Buscar por nombre', max_length=100)