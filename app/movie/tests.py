# python core impprt
import os
import json

# django core import 
from django.test import TestCase
from django.urls import reverse
from rest_framework.authtoken.models import Token
from model_mommy import mommy

# DRF import
from rest_framework_jwt.serializers import JSONWebTokenSerializer
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.test import APIClient


# Local imports
from .models import CustomUser
from .serializers import *



class MovieTest(TestCase):
    pass

class MovieAPITest(APITestCase):

    def test_list_movie(self):
        """
        Ensure that we can create a new movie
        """
        user = mommy.make(CustomUser)
        client = APIClient()
        client.force_authenticate(user=user)

        url = '/api/v1/tmovie/list/'
        response = client.get(url)
        data = {'status': True, 'data': []}
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, data)
    
    def test_create_movie(self):
        """
        Ensure that the movie is created
        """
        movie_data =  {
            "title": "Gol Maal",
            "movieId": "tt0079221",
            "release_date": 1979,
            "star_cast": "Amol Palekar, Bindiya Goswami, Deven Verma |",
            "rating": 8.5,
            "votes": "8.6 based on 17,328 user ratings",
            "links": "/title/tt0079221/",
            "trailer": "https://www.imdb.com//video/imdb/vi1489026841?playlistId=tt0079221",
            "summary": "Ramprasad is a recent college graduate who finds a job with a finicky man, Bhavani Shankar, who believes that a man without a mustache is a man without a character. Bhavani Shankar is also against any of his employees indulging in recreation of any kind. When Ramprasad is caught by his boss at a hockey match, he has to invent a twin brother, the clean-shaven Laxman Prasad, to save his job. When Bhavani's daughter falls in love with the clean-shaven Laxman Prasad, and insists on marrying him, and Bhavani insists she should marry Ramprasad, things take a whacky turn. A fake mother and a hilarious chase are other enjoyable features involved in this comedy.",
            "img_source": "https://m.media-amazon.com/images/M/MV5BMjA4OTczODgxNF5BMl5BanBnXkFtZTgwMDAzMTU2NDE@._V1_UY67_CR2,0,45,67_AL_.jpg",
            "taglines": "No Tagline Found",
            "certificate": "No Certificate Found",
            "trivia": "The Name of Bhavani Shankar's (Utpal Dutt's Bungalow) in the movie is Bindiya. Bindiya Gowsami, plays the role of Bhavani Shankar's daughter, Urmila in the movie.You can see that in the scene, where Amol Palekar gets caught and Bhavani Shankar is taking his car out of the gate to chase him        See more  »",
            "goofs": "No Goofs Found",
            "country": "No Country Origin Found",
            "language": "No Language Found",
            "budget": "No Budget Detail Found",
            "gross": "No Gross Record Found",
            "cumulative": "No Cumulative Record Found"
        }
        movie_serializer            = MovieSerializer(data=movie_data)

        if movie_serializer.is_valid():
            pass
            
        else:
            message = ''
            for error in movie_serializer.errors.values():
                message += " "
                message += error[0]
            print(message)
        
        movie = Movie(**movie_data)

        assert movie_data.get('title')             ==  movie_serializer.data.get('title')

    
    def test_watch_mark_api(self):
        user = mommy.make(CustomUser)
        
        movie_data =  {
            "id": 1,
            "title": "Gol Maal",
            "movieId": "tt0079221",
            "release_date": 1979,
            "star_cast": "Amol Palekar, Bindiya Goswami, Deven Verma |",
            "rating": 8.5,
            "votes": "8.6 based on 17,328 user ratings",
            "links": "/title/tt0079221/",
            "trailer": "https://www.imdb.com//video/imdb/vi1489026841?playlistId=tt0079221",
            "summary": "Ramprasad is a recent college graduate who finds a job with a finicky man, Bhavani Shankar, who believes that a man without a mustache is a man without a character. Bhavani Shankar is also against any of his employees indulging in recreation of any kind. When Ramprasad is caught by his boss at a hockey match, he has to invent a twin brother, the clean-shaven Laxman Prasad, to save his job. When Bhavani's daughter falls in love with the clean-shaven Laxman Prasad, and insists on marrying him, and Bhavani insists she should marry Ramprasad, things take a whacky turn. A fake mother and a hilarious chase are other enjoyable features involved in this comedy.",
            "img_source": "https://m.media-amazon.com/images/M/MV5BMjA4OTczODgxNF5BMl5BanBnXkFtZTgwMDAzMTU2NDE@._V1_UY67_CR2,0,45,67_AL_.jpg",
            "taglines": "No Tagline Found",
            "certificate": "No Certificate Found",
            "trivia": "The Name of Bhavani Shankar's (Utpal Dutt's Bungalow) in the movie is Bindiya. Bindiya Gowsami, plays the role of Bhavani Shankar's daughter, Urmila in the movie.You can see that in the scene, where Amol Palekar gets caught and Bhavani Shankar is taking his car out of the gate to chase him        See more  »",
            "goofs": "No Goofs Found",
            "country": "No Country Origin Found",
            "language": "No Language Found",
            "budget": "No Budget Detail Found",
            "gross": "No Gross Record Found",
            "cumulative": "No Cumulative Record Found"
        }
        movie = Movie(**movie_data)

        data = {}
        data['movie'] = movie.id
        data['action'] = 'watch_list'
        watch_serializer = WatchMarkSerializer(data=data)

        if watch_serializer.is_valid():
            watch = watch_serializer.create(watch_serializer.data, user)
            pass
        


        

