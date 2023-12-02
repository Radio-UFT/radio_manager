from django import forms
from programa.models import Programa

class FormularioPrograma(forms.ModelForm):
    class Meta:
        model = Programa
        fields = ['nome', 'horario', 'descricao', 'foto'] 
