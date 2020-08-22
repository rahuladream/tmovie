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
from .serializers import *

# API Logic Here


class ListMovieAPI(GenericAPIView):
    serializer_class = MovieSerializer
    # permission_classes = (IsAuthenticated,)

    def get(self, request):
        """
        List out all the movies
        """
        try:
            movie_obj        = Movie.objects.all()
            movie_serializer = MovieSerializer(movie_obj, many=True)
            movies = movie_serializer.data
            return Response({
                'status': True,
                'data': movies
            }, status=status.HTTP_200_OK) 
        except Exception as e:
            return Response({'status': False, 'message': str(e)},
                            status=status.HTTP_400_BAD_REQUEST)
    
    def post(self, request, format=None):
        """
        Create a movie database
        """
        try:
            pass
        except Exception as e:
            pass
        