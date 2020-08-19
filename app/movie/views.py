# python imports
import requests
import os
import datetime

# Django core imports
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.serializers import JSONWebTokenSerializer
from rest_framework_jwt.views import JSONWebTokenAPIView

# Local imports
from .models import *
from .utils import generate_jwt_token


# API Logic Here

class TestAppView(APIView):

    def get(self, request, format=None):

        try:
            sum = lambda x, y: x + y
            result = sum(11, 51)
            
            return Response({
                'status': True,
                'Response': 'On adding {} result is : {}'.format('11 + 51', result) },
                status = status.HTTP_200_OK
            )
        except Exception as e:
            return Response({
                'status': False,
                'message': str(e)},
                status = status.HTTP_400_BAD_REQUEST
            )
