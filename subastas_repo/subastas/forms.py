from django import forms
from django.core.urlresolvers import reverse
from django.db.models import Q

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Reset, Layout, Div

from .models import Acta, Grupo, Lote, Rodado, Subasta
from personas.models import Persona, Profesional


class ActaForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ActaForm, self).__init__(*args, **kwargs)

        current_subasta = Subasta.objects.get_current()

        # Mostrar solo las personas inscriptas
        self.fields['persona'].queryset = current_subasta.personas.all()

        # Mostrar solo los profesionales de la subasta
        self.fields['profesionales'].queryset = current_subasta.profesionales.all()

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
        self.fields['profesionales'].queryset = Profesional.objects \
            .exclude(titulo__nombre__iexact='martillero')

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
                'profesionales')
        )

    class Meta:
        fields = [
            'numero',
            'fecha_hora',
            'decreto',
            'domicilio',
            'profesionales',
        ]
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
    lotes = forms.ModelMultipleChoiceField(
        Lote.objects.none(),
        required=False,
        widget=forms.CheckboxSelectMultiple
    )

    def __init__(self, *args, **kwargs):
        self.kw = kwargs
        self.lotes = kwargs.pop('lotes', None)

        super(GrupoForm, self).__init__(*args, **kwargs)
        if self.lotes:
            self.fields['lotes'].queryset = self.lotes

        self.fields['martillero'].queryset = Profesional.objects \
            .filter(titulo__nombre__iexact='martillero')

        instance = kwargs.get('instance', None)
        if instance:
            form_action = reverse("subastas:grupos_update",
                                  args=(self.instance.id, ))
        else:
            form_action = reverse("subastas:grupos_create")

        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.form_action = form_action
        self.helper.add_input(Submit('grupo_submit', 'Guardar'))
        self.helper.add_input(Reset('grupo_reset', 'Limpiar',
                              css_class='btn-default'))
        self.helper.layout = Layout(
            Div('numero',
                'martillero',
                'lotes')
        )

    def clean_numero(self):
        numero = self.cleaned_data.get('numero')
        instance = self.kw.get('instance', None)  # If update
        if instance and numero != instance.numero:
            subasta = Subasta.objects.get_current()
            if Grupo.objects.filter(subasta=subasta,
                                    numero=numero).exists():
                raise forms.ValidationError("Este grupo ya existe.")
        return numero

    class Meta:
        fields = [
            "numero",
            "martillero",
            "lotes",
        ]
        model = Grupo


class LoteForm(forms.ModelForm):
    rodados = forms.ModelMultipleChoiceField(
        Rodado.objects.none(),
        required=False,
        widget=forms.CheckboxSelectMultiple
    )

    def __init__(self, *args, **kwargs):
        self.rodados_query = kwargs.pop('rodados_query', None)
        super(LoteForm, self).__init__(*args, **kwargs)

        if self.rodados_query:
            self.fields['rodados'].queryset = self.rodados_query

        instance = kwargs.get('instance', None)
        if instance:
            form_action = reverse("subastas:lotes_update",
                                  args=(instance.id, ))
        else:
            form_action = reverse("subastas:lotes_create")

        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.form_action = form_action
        self.helper.add_input(Submit('lote_submit', 'Guardar'))
        self.helper.add_input(Reset('lote_reset', 'Limpiar',
                              css_class='btn-default'))
        self.helper.layout = Layout(
            Div('numero',
                'rodados')
        )

    def clean_numero(self):
        numero = self.cleaned_data.get('numero')
        if Lote.objects.filter(grupo=None,
                               numero=numero).exists():
            raise forms.ValidationError("Este Lote ya existe.")
        return numero

    class Meta:
        fields = [
            'numero',
            'rodados',
        ]
        model = Lote
