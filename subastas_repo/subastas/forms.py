from django import forms

from django.core.urlresolvers import reverse

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Reset, Layout, Div

from .models import Subasta


class SubastaForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(SubastaForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.form_action = reverse("subastas:create")
        self.helper.add_input(Submit('job_submit', 'Guardar'))
        self.helper.add_input(Reset('job_reset', 'Limpiar',
                              css_class='btn-default'))
        self.helper.layout = Layout(
            Div('numero',
                'fecha_hora',
                'decreto',
                'domicilio',
                'profesionales',
                'bienes')
        )

    class Meta:
        fields = ['numero',
                  'fecha_hora',
                  'decreto',
                  'domicilio',
                  'profesionales',
                  'bienes']
        model = Subasta
