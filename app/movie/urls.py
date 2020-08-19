# -*- coding: utf-8 -*

from __future__ import print_function, unicode_literals
# Python Imports
import logging

# Django Core Imports
from django.conf.urls import url

# Django rest_framework imports

# Local Imports

from .views import (
                TestAppView
                )
from .swagger import schema_view

app_name = 'movie'

urlpatterns = [
    url(r'^test/$', TestAppView.as_view(), name='test_app_api'),

    url(r'^docs/$', schema_view, name="schema_view"),

]