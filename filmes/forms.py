from django import forms
from .models import Filme,Buscar


class FilmeForm(forms.ModelForm):
    class Meta:
        model = Filme
        fields = ('nome', 'categoria', 'duracao', 'preco')
        
class BuscarForm(forms.ModelForm):
    class Meta:
        model = Buscar
        fields = ('nome_filme',)

