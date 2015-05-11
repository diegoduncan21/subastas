from django import forms

from django.core.urlresolvers import reverse

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Reset, Layout, Div

from .models import Acta, Subasta
from personas.models import Persona


class ActaForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ActaForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "POST"
        self.helper.form_action = reverse("subastas:actas_create")
        self.helper.add_input(Submit('job_submit', 'Guardar'))
        self.helper.add_input(Reset('job_reset', 'Limpiar',
                              css_class='btn-default'))
        self.helper.layout = Layout(
            Div('bien_rodado',
                'persona',
                'profesionales',
                'descripcion')
        )

    class Meta:
        fields = ['bien_rodado',
                  'persona',
                  'profesionales',
                  'descripcion']
        model = Acta


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


class InscriptionForm(forms.ModelForm):
    personas = forms.ModelMultipleChoiceField(Persona.objects.all(),
                                              label='Inscriptos de subastas anteriores.',
                                              required=True,
                                              widget=forms.CheckboxSelectMultiple())

    class Meta:
        fields = ['personas']
        model = Subasta

    def __init__(self, *args, **kwargs):
        current_subasta = kwargs.pop('instance')
        super(InscriptionForm, self).__init__(*args, **kwargs)
        choices = Persona.objects.exclude(
            id__in=current_subasta.personas.values_list('id', flat=True)) \
            .order_by('apellidos')
        self.fields['personas'].queryset = choices
