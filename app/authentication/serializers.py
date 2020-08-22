# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Django imports.
from django.db import transaction
# Rest Framework imports.
from rest_framework import serializers

# local imports.
from .models import CustomUser


# Python imports.
# Third Party Library imports


class UserCreateSerializer(serializers.ModelSerializer):
    """
    Serializer to get thedata and 
    create user
    """

    password = serializers.CharField(write_only=True)

    def validate(self, data, *args, **kwargs):
        return super(UserCreateSerializer, self).validate(data, *args, **kwargs)

    @transaction.atomic
    def create(self, validated_data):
        username = validated_data['username']
        first_name = validated_data['first_name']
        last_name = validated_data['last_name']
        email = validated_data['email']
        user = CustomUser.objects.create(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'password', 'first_name', 'last_name')


class UserListSearialzer(serializers.ModelSerializer):
    """
    Listing the uSer int serialized format
    """

    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'first_name', 'last_name', 'email')
