from django import forms
from django.forms import ModelForm

class RegleForm(ModelForm):
    Nom = forms.CharField(required=False)
    TypeRegle = forms.CharField(required=False)
    Corps = forms.TextInput()
    LibParam1 = forms.CharField(required=False)
    LibParam2 = forms.CharField(required=False)
    LibParam3 = forms.CharField(required=False)
    LibParam4 = forms.CharField(required=False)
    LibParam5 = forms.CharField(required=False)
    LibParam6 = forms.CharField(required=False)
    LibParam7 = forms.CharField(required=False)
    LibParam8 = forms.CharField(required=False)
    LibParam9 = forms.CharField(required=False)
    LibParam10 = forms.CharField(required=False)

