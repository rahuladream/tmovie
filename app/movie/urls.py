# -*- coding: utf-8 -*

from __future__ import print_function, unicode_literals

# Django Core Imports
from django.conf.urls import url

from .views import (
    ListMovieAPI,
    WatchMarkAPI,
    WatchListAPI,
    WatchedListAPI,
    SingleMovieAPI
)

# Python Imports
# Django rest_framework imports
# Local Imports


app_name = 'movie'

urlpatterns = [
    url(r'^watch_or_watched/$', WatchMarkAPI.as_view(), name='watch-mark-api'),
    url(r'^movie_list/(?P<pk>\d+)/$', SingleMovieAPI.as_view(), name='movie-get-single-api'),
    url(r'^movie_lists/$', ListMovieAPI.as_view(), name='movie-get-all-api'),
    url(r'^my_watch_list/$', WatchListAPI.as_view(), name='movie-get-all-watch-list'),
    url(r'^my_watched_list/$', WatchedListAPI.as_view(), name='movie-get-all-watched-list')

]
