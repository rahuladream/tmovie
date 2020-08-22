# python imports
import requests
import os
import datetime

# Django imports
from django.core.exceptions import ObjectDoesNotExist, ValidationError

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


__author__ = 'Rahul'


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


class LoginAPIView(JSONWebTokenAPIView):
    serializer_class = JSONWebTokenSerializer

    __doc__ = "Login In API for user which returns token"

    @staticmethod
    def post(request):
        try:
            serializer = JSONWebTokenSerializer(data=request.data)
            if serializer.is_valid():
                serializer_data = serializer.validate(request.data)

                user = CustomUser.objects.get(username=request.data.get('username'))
                return Response( {
                    'status': True,
                    'token': serializer_data['token']},
                    status=status.HTTP_200_OK )
            else:
                message = ''
                for error in serializer.errors.values():
                    message += " "
                    message += error[0]
                return Response({
                    'status': False,
                    'message': message
                }, status=status.HTTP_400_BAD_REQUEST)
        except (AttributeError, ObjectDoesNotExist):
            return Response({
                'status': False,
                'message': 'User does not exist'
            }, status=status.HTTP_400_BAD_REQUEST)


class LogoutView(APIView):
    permission_classes = (IsAuthenticated, )

    @staticmethod
    def post(request):
        """
        Logout API for User
        """
        try:
            request.user.auth_token.delete()
            return Response({
                'status': True,
                'message': 'Logout successful',
            }, status=status.HTTP_200_OK)
        except (AttributeError, ObjectDoesNotExist):
            return Response({
                'status': False,
            }, status=status.HTTP_400_BAD_REQUEST)