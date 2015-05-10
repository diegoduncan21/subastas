# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

from personas import views

urlpatterns = patterns('',
    url(
        regex=r'^asociar/(?P<subasta_id>\d+)$',
        view=views.asociar,
        name='asociar'
    ),
    url(
        regex=r'^desasociar/(?P<subasta_id>\d+)/(?P<persona_id>\d+)$',
        view=views.desasociar,
        name='desasociar'
    ),
    url(
        regex=r'^profesionales/$',
        view=views.ProfesionalListView.as_view(),
        name='profesionales_list'
    ),
    url(
        regex=r'^profesionales/create/$',
        view=views.ProfesionalCreateView.as_view(),
        name='profesionales_create'
    ),
    url(
        regex=r'^profesionales/update/(?P<pk>\d+)/$',
        view=views.ProfesionalUpdateView.as_view(),
        name='profesionales_update'
    ),
    url(
        regex=r'^profesionales/delete/(?P<pk>\d+)/$',
        view=views.ProfesionalDeleteView.as_view(),
        name='profesionales_delete'
    ),
)
