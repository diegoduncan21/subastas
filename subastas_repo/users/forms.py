# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.models import Permission
from django.core.urlresolvers import reverse

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Reset, Layout, Div

from .models import User


class UserForm(forms.ModelForm):

    class Meta:
        # Set this form to use the User model.
        model = User

        # Constrain the UserForm to just these fields.
        fields = ("first_name", "last_name")


class CreateUserForm(forms.ModelForm):
    perfil = forms.ModelChoiceField(
        queryset=Permission.objects.filter(codename__in=['acreditador',
                                                         'actero',
                                                         'administrador']))
    password = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())

    def __init__(self, *args, **kwargs):
        super(CreateUserForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('user_submit', 'Guardar'))
        self.helper.add_input(Reset('user_reset', 'Limpiar',
                              css_class='btn-default'))

        self.username = None
        if 'instance' in kwargs and kwargs.get('instance') is not None:
            self.username = kwargs['instance'].username

    class Meta:
        # Set this form to use the User model.
        model = User
        fields = ("first_name",
                  "last_name",
                  "username",
                  "password",
                  "password2",
                  "perfil")

    def clean_username(self):
        """Check if the username already exists, and is not his email"""

        username = self.cleaned_data['username']

        if self.username:
            if self.username != username:
                if User.objects.filter(username=username).exists():
                    raise forms.ValidationError("El nombre de usuario ya esta en uso.")
        return username

    def clean(self):
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')

        if password and password != password2:
            raise forms.ValidationError("Las contraseñas no son iguales.")

        return self.cleaned_data
