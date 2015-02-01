# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

from users import views

urlpatterns = patterns('',
    # URL pattern for the UserListView  # noqa
    url(
        regex=r'^$',
        view=views.UserListView.as_view(),
        name='list'
    ),
    # URL pattern for the UserRedirectView
    url(
        regex=r'^~redirect/$',
        view=views.UserRedirectView.as_view(),
        name='redirect'
    ),
    # URL pattern for the UserDetailView
    url(
        regex=r'^(?P<username>[\w.@+-]+)/$',
        view=views.UserDetailView.as_view(),
        name='detail'
    ),
    # URL pattern of the UserCreateView
    url(
        regex=r'^~create/$',
        view=views.create_user,
        name='create'
    ),

    # URL patter of the UserUpdateSubastasView
    url(
        regex=r'^~update/(?P<user_id>\d+)/$',
        view=views.update_user,
        name='update'
    ),
)
