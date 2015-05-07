from django import forms
from django.core.urlresolvers import reverse

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Reset, Layout, Div

from .models import Persona, Profesional


class ProfesionalForm(forms.ModelForm):
    class Meta:
        model = Profesional


class PersonaForm(forms.ModelForm):
    nombres = forms.CharField()
    apellidos = forms.CharField()
    razon_social = forms.CharField()
    dni = forms.CharField()
    cuit = forms.CharField()

    class Meta:
        model = Persona
        fields = ['nombres',
                  'apellidos',
                  'razon_social',
                  'dni',
                  'cuit',
                  'domicilio',
                  'telefono']

    def __init__(self, *args, **kwargs):
        super(PersonaForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.form_action = reverse('subastas:acreditadores')
        self.helper.add_input(Submit('user_submit', 'Guardar'))
        self.helper.add_input(Reset('user_reset', 'Limpiar',
                              css_class='btn-default'))
        self.helper.layout = Layout(
            Div('nombres',
                'apellidos',
                'razon_social',
                'dni',
                'cuit',
                'domicilio',
                'telefono')
        )
