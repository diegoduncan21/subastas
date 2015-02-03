from django import forms

from .models import Profesional


class ProfesionalForm(forms.ModelForm):
    class Meta:
        model = Profesional
