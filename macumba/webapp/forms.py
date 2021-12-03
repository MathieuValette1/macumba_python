from django import forms

from .models import Victime, Sauveteur, Bateau


class VictimeForm(forms.ModelForm):
    class Meta:
        model = Victime
        fields = {'isEnfant', 'isAdo', 'isAlive'}
        labels = {'isEnfant': ("C'est un enfant ?"), 'isAdo': ("C'est un ado ?"), 'isAlive': ("La victime est en vie ?")}

class SauveteurForm(forms.ModelForm):
    class Meta:
        model = Sauveteur
        fields = '__all__'


class BateauForm(forms.ModelForm):
    class Meta:
        model = Bateau
        fields = '__all__'

