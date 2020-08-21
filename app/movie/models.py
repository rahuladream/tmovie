# Python Core Imports
import os
import json
import datetime

# Django Imports
from django.utils import timezone
from django.db import models
from django.utils.translation import ugettext_lazy as _


YEAR_CHOICES = []
for r in range(1700, (datetime.datetime.now().year + 1)):
    YEAR_CHOICES.append((r,r))


class Movie(models.Model):
    title           = models.CharField(_('Movie Title'),max_length=200)
    movieId         = models.CharField(_('Movie Unique ID'),max_length=20)
    release_date    = models.IntegerField(_('Release Year'), choices=YEAR_CHOICES)
    star_cast       = models.CharField(_('Movie Start Cast'), max_length=255)
    rating          = models.FloatField(_('Movie Rating'))
    votes           = models.IntegerField(_('Movie Votes'))
    links           = models.CharField(_('Movie Detail Link'), max_length=100)
    trailer         = models.CharField(_('Trailer Link'), max_length=200)
    summary         = models.TextField(_('Movie Summary'))
    taglines        = models.TextField(_('Movie TagLines'), blank=True, null=True)
    certificate     = models.CharField(_('Movie Certificate'), max_length=2, blank=True, null=True)
    trivia          = models.CharField(_('Movie Trivia'), max_length=200, blank=True, null=True)
    goofs           = models.CharField(_('Movie Goofs'), max_length=200, blank=True, null=True)
    country         = models.CharField(_('Movie Country'), max_length=100, blank=True, null=True)
    language        = models.CharField(_('Movie Language'), max_length=100, blank=True, null=True)
    budget          = models.CharField(_('Movie Total Budget'), max_length=50, blank=True, null=True)
    gross           = models.CharField(_('Movie Total Gross Amount'), max_length=50, null=True, blank=True)
    cumulative      = models.CharField(_('Movie Total Cumulative Amount'), max_length=50, null=True, blank=True)
    movie_dump      = models.TextField(_('Store more information here'), null=True, blank=True)

    class Meta:
        verbose_name = _('movie')
        verbose_name_plural = _('movies')
    
    def get_avg_rating(self):
        """
        Convert float rating into readable format
        """
        return self.rating
    
    def __unicode__(self):
        return f'Movie Title: {self.title}'


