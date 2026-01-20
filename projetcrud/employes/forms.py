from django import forms
from .models import Employe

class Employeform(forms.ModelForm):
    class Meta:
        model = Employe
        fields = ['nom', 'prenom', 'email', 'adresse', 'telephone']