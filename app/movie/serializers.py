#!/usr/bin/env python

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Python imports.
import logging
import datetime
import calendar

# Django imports.
from django.db import transaction

# Rest Framework imports.
from rest_framework import serializers

# Third Party Library imports
from .models import Movie, Watch

class MovieSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Movie
        exclude = ('movie_dump',)
        # fields = '__all__'


class WatchMarkSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Watch
        fields = ('movie', 'action')

    def create(self, validated_data, usr):
        movie_obj                       = Movie.objects.get(id=validated_data['movie'])
        return Watch.objects.create(user=usr, movie=movie_obj, action=validated_data['action'])

    def update(self, validated_data, usr):
        movie_obj                       = Movie.objects.get(id=validated_data['movie'])
        return Watch.objects.filter(user=usr, movie=movie_obj).update(**validated_data)
        

class WatchListSerializer(serializers.ModelSerializer):
    movie = MovieSerializer(read_only=True)
    class Meta:
        model = Watch
        fields = ['movie', 'action']


class WatchedListSerializer(serializers.ModelSerializer):
    movie = MovieSerializer(read_only=True)
    class Meta:
        model = Watch
        fields = ['movie', 'action']