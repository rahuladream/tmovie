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
                TestAppView
                )




app_name = 'movie'

urlpatterns = [
    url(r'^test/$', TestAppView.as_view(), name='test_app_api'),

   

]