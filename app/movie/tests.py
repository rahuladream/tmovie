# python core impprt
import os
import json

# django core import 
from model_mommy import mommy
from django.test import TestCase

# DRF import
from rest_framework_jwt.serializers import JSONWebTokenSerializer

# Local imports
from .models import CustomUser
from .serializers import UserCreateSerializer, UserListSearialzer