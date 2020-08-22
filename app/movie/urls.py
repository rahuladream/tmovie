# -*- coding: utf-8 -*

from __future__ import print_function, unicode_literals
# Python Imports
import logging

# Django Core Imports
from django.conf.urls import url

# Django rest_framework imports
from rest_framework import permissions

# Local Imports
from .constants import *

from .views import (
                ListMovieAPI,
                WatchMarkAPI
                )




app_name = 'movie'

urlpatterns = [
    url(r'^mark/$', WatchMarkAPI.as_view(), name='watch-mark-api'),
    url(r'^list/$', ListMovieAPI.as_view(), name='movie-get-all-api')
   

]