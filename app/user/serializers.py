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

# local imports.
from .models import CustomeUser


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def validate(self, data, *args, **kwargs):
        return super(UserCreateSerializer, self).validate(data, *args, **kwargs)
    
    @transaction.atomic
    def create(self, validated_data):
        username = validated_data['username']
        first_name = validated_data['first_name']
        last_name = validated_data['last_name']
        role = validated_data['role']
        email = validated_data['email']
        user = CustomeUser.objects.create(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
    
    class Meta:
        model = CustomeUser
        fields = ('email', 'id', 'password', 'first_name', 'last_name', 'role')
