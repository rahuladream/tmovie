# python imports


from rest_framework import permissions
# Django core imports
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

# Local imports
from .serializers import *

# API Logic Here

__author__ = 'Rahul'


class ListMovieAPI(GenericAPIView):
    serializer_class = MovieSerializer
    pagination_class   = StandardPagination
    permission_classes = (IsAuthenticated,)
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    

    def get(self, request):
        """
        List out all the movies
        """
        try:
            movie_obj = Movie.objects.all()
            movie_serializer = MovieSerializer(movie_obj, many=True)
            movies = movie_serializer.data
            return Response({
                'status': True,
                'data': movies
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'status': False, 'message': str(e)},
                            status=status.HTTP_400_BAD_REQUEST)


class SingleMovieAPI(GenericAPIView):
    serializer_class = MovieSerializer

    permission_classes = (IsAuthenticated,)
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, pk, format=None):

        """
        Individual Movie fetch
        """

        try:
            movie_obj = Movie.objects.get(pk=pk)
            serializer = MovieSerializer(movie_obj)

            return Response({
                'status': True,
                'data': serializer.data
            }, status=status.HTTP_200_OK)
        except Movie.DoesNotExist:
            return Response({'status': False, 'message': 'Query not found'},
                            status=status.HTTP_400_BAD_REQUEST)


class WatchMarkAPI(APIView):
    serializer_class = WatchMarkSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request, format=None):
        """
        Mark a movie as watched or add it to watch list
        """
        try:
            data = request.data
            serializer = WatchMarkSerializer(data=data)

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
        Update already mark user
        """
        try:
            data = request.data
            movie_obj = Movie.objects.get(id=request.data.get('movie'))
            action = request.data.get('action')
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

    def delete(self, request, format=None):
        """
        Delete the watch/watched list data
        """
        try:
            data = request.data
            movie_obj = Movie.objects.get(id=request.data.get('movie'))
            watch_obj = Watch.objects.get(user=request.user, movie=movie_obj)
            watch_obj.delete()

            return Response({
                'status': True,
                'message': 'Movie deleted from watch/watched list.'
            }, status=status.HTTP_200_OK)
        except Watch.DoesNotExist:
            return Response({
                'status': False,
                'message': 'Requested movie does not exist in watch list.'
            }, status=status.HTTP_400_BAD_REQUEST)


class WatchListAPI(APIView):
    serializer_class = WatchListSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        try:
            watch_obj = Watch.objects.filter(user=request.user, action="watch_list")
            watch_serializer = WatchListSerializer(watch_obj, many=True)
            movies = watch_serializer.data
            return Response({
                'status': True,
                'data': movies
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'status': False, 'message': str(e)},
                            status=status.HTTP_400_BAD_REQUEST)


class WatchedListAPI(APIView):
    serializer_class = WatchedListSerializer

    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        try:
            watch_obj = Watch.objects.filter(user=request.user, action="watched_list")
            watch_serializer = WatchListSerializer(watch_obj, many=True)
            movies = watch_serializer.data
            return Response({
                'status': True,
                'data': movies
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'status': False, 'message': str(e)},
                            status=status.HTTP_400_BAD_REQUEST)
