from django import forms
from django.core.urlresolvers import reverse
from django.db.models import Q

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Reset, Layout, Div

from .models import Acta, Grupo, Rodado, Subasta
from personas.models import Persona


class ActaForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ActaForm, self).__init__(*args, **kwargs)

        # Mostrar solo las personas inscriptas
        current_subasta = Subasta.objects.get_current()
        self.fields['persona'].queryset = current_subasta.personas.all()

        self.helper = FormHelper()
        self.helper.form_method = "POST"
        self.helper.form_action = reverse("subastas:actas_create")
        self.helper.add_input(Submit('job_submit', 'Guardar'))
        self.helper.add_input(Reset('job_reset', 'Limpiar',
                              css_class='btn-default'))
        self.helper.layout = Layout(
            Div('lote',
                'persona',
                'profesionales',
                'descripcion')
        )

    class Meta:
        fields = ['lote',
                  'persona',
                  'profesionales',
                  'descripcion']
        model = Acta


class SubastaForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(SubastaForm, self).__init__(*args, **kwargs)
        # Mostrar solo los bienes no subastados
        self.fields['bienes'].queryset = Rodado.objects.no_subastados()

        instance = kwargs.get('instance', None)
        if instance:
            form_action = reverse("subastas:update",
                                       args=(self.instance.id, ))
        else:
            form_action = reverse("subastas:create")

        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.form_action = form_action
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
        current_subasta = kwargs.pop('instance', None)
        query = kwargs.pop('query', None)
        super(InscriptionForm, self).__init__(*args, **kwargs)

        personas = Persona.objects.exclude(
            id__in=current_subasta.personas.values_list('id', flat=True))
        if query:
            personas = personas.filter(Q(nombres__icontains=query) |
                                       Q(apellidos__icontains=query) |
                                       Q(dni__icontains=query))
        self.fields['personas'].queryset = personas.order_by('apellidos')


class RodadoForm(forms.ModelForm):
    class Meta:
        fields = ['tipo',
                  'numero_inventario',
                  'descripcion',
                  'marca',
                  'modelo',
                  'chasis',
                  'motor',
                  'dominio',
                  'anio',
                  'precio_base',
                  'precio_venta']
        model = Rodado


class GrupoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(GrupoForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.form_action = reverse("subastas:grupos_create")
        self.helper.add_input(Submit('grupo_submit', 'Guardar'))
        self.helper.add_input(Reset('grupo_reset', 'Limpiar',
                              css_class='btn-default'))
        self.helper.layout = Layout(
            Div('numero',
                'martillero')
        )

    class Meta:
        model = Grupo
