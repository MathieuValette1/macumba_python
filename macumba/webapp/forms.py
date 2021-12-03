from django.forms import forms

from macumba.webapp.models import Victime, Sauveteur, Bateau


class VictimeForm(forms.ModelForm):
    class Meta:
        model = Victime
        labels = {'isEnfant': ("C'est un enfant ?"), 'isAdo': ("C'est un ado ?"), 'isAlive': ("La victime est en vie ?")}

class SauveteurForm(forms.ModelForm):
    class Meta:
        model = Sauveteur


class BateauForm(forms.ModelForm):
    class Meta:
        model = Bateau
