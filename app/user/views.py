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
from .serializers import *




class RegistrationAPIView(APIView):
    serializer_class = UserCreateSerializer
    __doc__ = "Registration API for newly User"

    def post(self, request, *args, **kwargs):
        try:
            user_serializer = UserCreateSerializer(data=request.data)
            if user_serializer.is_valid():
                user = user_serializer.save()
                data = generate_jwt_token(user, user_serializer.data)
                return Response(data, status=status.HTTP_200_OK)
            else:
                message = ''
                for error in user_serializer.errors.values():
                    message += " "
                    message += error[0]
                return Response({
                    'status': False,
                    'message': message},
                    status=status.HTTP_400_BAD_REQUEST
                    )
        except Exception as e:
            return Response({'status': False,
                             'message': str(e)},
                                status=status.HTTP_400_BAD_REQUEST)
