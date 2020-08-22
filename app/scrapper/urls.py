# -*- coding: utf-8 -*

from __future__ import print_function, unicode_literals

# Django Core Imports
from django.conf.urls import url

# Local Imports
from .views import (
    SyncData
)

# Python Imports
# Django rest_framework imports


app_name = 'movie'

urlpatterns = [
    url(r'^sync_imdb/$', SyncData.as_view(), name='sync-imdb-data'),

]
