# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.models import Permission

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

    class Meta:
        # Set this form to use the User model.
        model = User
        fields = ("first_name", "last_name", "perfil")
