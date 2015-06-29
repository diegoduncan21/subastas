# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

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
        view=views.SubastaUpdateView.as_view(),
        name='update'
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
        regex=r'^imprimir/(?P<pk>\d+)$',
        view=views.ActaPrintView.as_view(),
        name='print'
    ),
    url(
        regex=r'^acreditadores$',
        view=views.AcreditadorHomeView.as_view(),
        name='acreditadores'
    ),
    url(
        regex=r'^bienes$',
        view=views.RodadoListView.as_view(),
        name='rodados'
    ),
    url(
        regex=r'^bienes/nuevo/$',
        view=views.RodadoCreateView.as_view(),
        name='rodados_create'
    ),
    url(
        regex=r'^bienes/editar/(?P<pk>\d+)$',
        view=views.RodadoUpdateView.as_view(),
        name='rodados_update'
    ),
    url(
        regex=r'^bienes/nuevo/xlsx$',
        view=views.upload_xlsx,
        name='rodados_nuevo_xlsx'
    ),
    url(
        regex=r'^grupos$',
        view=views.GrupoListView.as_view(),
        name='grupos'
    ),
    url(
        regex=r'^grupos/nuevo/$',
        view=views.GrupoCreateView.as_view(),
        name='grupos_create'
    ),
    # Sin permisos
    url(
        regex=r'^sin_permisos$',
        view=TemplateView.as_view(
            template_name='subastas/sin_permisos.html'),
        name='sin_permisos'
    ),
)
