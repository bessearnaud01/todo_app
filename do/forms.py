from django import forms # On importe la librairie forms.

from .models import Task

class TacheForm(forms.ModelForm):
    tache = forms.CharField(max_length=150, widget=forms.TextInput(attrs={ #attrs est dictionnaire qui va contenir tout nos values
        'placeholder' : 'Enter la tache',
        'class' : 'form-control form-control-lg' # form-control-lg rend le formulaire plus grand 
    }))
    # J'utilise django qui permet aux gens d'ajouter des paramètres supplémentaires à une classe en utilisant class Meta #
    class Meta:
        model = Task # tache serait égale à notre modele 
        fields = [
            'tache'
        ]