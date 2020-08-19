# -*- coding: utf-8 -*

from __future__ import print_function, unicode_literals
# Python Imports
import logging

# Django Core Imports
from django.conf.urls import url

# Django rest_framework imports
from rest_framework import permissions




from .views import (
                RegistrationAPIView,
                LoginAPIView
                )


app_name = 'user'

urlpatterns = [

    url(r'^register/$', RegistrationAPIView.as_view(), name='register-api'),
    url(r'^login/$', LoginAPIView.as_view(), name='login-api'),


]