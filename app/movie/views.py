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


# class ProjectAPIView(GenericAPIView):
#     serializer_class = ProjectSerializer
#     permission_classes = (IsAuthenticated,)

#     def get(self, request):
#         """
#         List out all the movies
#         """
#         try:
#             pass
#         except Exception as e:
#             pass
    
#     def post(self, request, format=None):
#         """
#         Create a movie database
#         """
#         try:
#             pass
#         except Exception as e:
#             pass
        