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

# Yet another swagger import 
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from .views import (
                TestAppView
                )


schema_view = get_schema_view(
   openapi.Info(
      title=DOCS_TITLE,
      default_version=DOCS_VERSION,
      description=DOCS_DESCRIPTION,
      terms_of_service=DOCS_TERM_SERVICE,
      contact=openapi.Contact(email=DOCS_CONTACT_HEAD),
      license=openapi.License(name=DOCS_LICENSE),
   ),
   public=DOCS_VISIBLE_PUBLIC,
   permission_classes=(permissions.AllowAny,),
)

app_name = 'movie'

urlpatterns = [
    url(r'^test/$', TestAppView.as_view(), name='test_app_api'),

    

    url(r'^docs(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='docs-json'),
    url(r'^docs/$', schema_view.with_ui('swagger', cache_timeout=0), name='docs-ui'),
    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),



]