# Python Core Imports
import os
import json
import datetime

# Django Imports
from django.utils import timezone
from django.db import models
from django.utils.translation import ugettext_lazy as _
from app.authentication.models import CustomUser 


class ScrapperURL(models.Model):
    imdb_url              =          models.CharField(help_text = "'https://imdb.com/first_url'", max_length=300)
    created_at            =          models.DateTimeField(auto_now_add=True)
    updated_at            =          models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.imdb_url