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
        regex=r'^create/$',
        view=views.SubastaCreateView.as_view(),
        name='create'
    ),
    url(
        regex=r'^edit/(?P<pk>\d+)$',
        view=views.SubastaEditView.as_view(),
        name='edit'
    ),
    url(
        regex=r'^actas$',
        view=views.ActaListView.as_view(),
        name='actas_list'
    ),
    url(
        regex=r'^actas/create/$',
        view=views.ActaCreateView.as_view(),
        name='actas_create'
    ),
)
