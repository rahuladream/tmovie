# python imports
import requests
import os
import datetime
from collections import OrderedDict 


# Django core imports
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.serializers import JSONWebTokenSerializer
from rest_framework_jwt.views import JSONWebTokenAPIView
from rest_framework import permissions


# Local imports
from .models import *
from .serializers import *

# API Logic Here


class ListMovieAPI(GenericAPIView):
    serializer_class = MovieSerializer
    # permission_classes = (IsAuthenticated,)
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]


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


class WatchMarkAPI(APIView):
    serializer_class = WatchMarkSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request, format=None):
        """
        Mark a movie as watched or add it to watch list
        """
        try:
            data                = request.data
            serializer          = WatchMarkSerializer(data=data)

            if serializer.is_valid():
                watch = serializer.create(serializer.data, request.user)
                return Response({
                    'status': True,
                    'message': 'Movie added to watch/watched list'
                }, status=status.HTTP_201_CREATED)
            else:
                message = ''
                for error in serializer.errors.values():
                    message += " "
                    message += error[0]
                return Response({
                    'status': False,
                    'message': message
                }, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({
                'status': False,
                'message': str(e)
            }, status=status.HTTP_400_BAD_REQUEST)
        
    
    def put(self, request, format=None):
        """
        Update already marke user
        """
        try:
            data            = request.data
            movie_obj       = Movie.objects.get(id=request.data.get('movie'))
            action          = request.data.get('action')
            is_update = Watch.objects.filter(user=request.user, movie=movie_obj).update(action=action)
            
            if is_update:
                return Response({
                    'status': True,
                    'message': 'Movie updated to watch/watched list.'
                }, status=status.HTTP_200_OK)
            else:
                return Response({
                    'status': False,
                    'message': 'We are unable to update the request.'
                }, status=status.HTTP_400_BAD_REQUEST)

            
        except Exception as e:
            return Response({
                'status': False,
                'message': str(e)
            }, status=status.HTTP_400_BAD_REQUEST)

