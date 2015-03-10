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
        regex=r'^subastas/create/$',
        view=views.SubastaCreateView.as_view(),
        name='create'
    ),
)
