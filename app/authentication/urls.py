# -*- coding: utf-8 -*

from __future__ import print_function, unicode_literals

# Django Core Imports
from django.conf.urls import url

from .views import (
    RegistrationAPIView,
    LoginAPIView
)

# Python Imports
# Django rest_framework imports


app_name = 'user'

urlpatterns = [

    url(r'^register/$', RegistrationAPIView.as_view(), name='register-api'),
    url(r'^login/$', LoginAPIView.as_view(), name='login-api'),
    url(r'^logout/$', LoginAPIView.as_view(), name='logout-api'),

]
