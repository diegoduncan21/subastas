# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import patterns, include, url

from . import views

urlpatterns = patterns('subastas.views',
    url(
        regex=r'^$',
        view=views.SubastaListView.as_view(),
        name='list'
    ),
    url(
        regex=r'^nuevo/$',
        view=views.SubastaCreateView.as_view(),
        name='create'
    ),
    url(
        regex=r'^editar/(?P<pk>\d+)$',
        view=views.SubastaEditView.as_view(),
        name='edit'
    ),
    url(
        regex=r'^cerrar/(?P<subasta_id>\d+)$',
        view=views.cerrar_subasta,
        name='close'
    ),
    url(
        regex=r'^actas$',
        view=views.ActaListView.as_view(),
        name='actas'
    ),
    url(
        regex=r'^actas/nuevo/$',
        view=views.ActaCreateView.as_view(),
        name='actas_create'
    ),
    url(
        regex=r'^acreditadores$',
        view=views.AcreditadorHomeView.as_view(),
        name='acreditadores'
    ),
)
