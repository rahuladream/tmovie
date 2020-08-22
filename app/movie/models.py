# Python Core Imports
import datetime

# Django Imports
from django.db import models
from django.utils.translation import ugettext_lazy as _

from app.authentication.models import CustomUser

YEAR_CHOICES = []
for r in range(1700, (datetime.datetime.now().year + 1)):
    YEAR_CHOICES.append((r,r))


class Movie(models.Model):
    title           = models.CharField(_('Movie Title'),max_length=200)
    movieId         = models.CharField(_('Movie Unique ID'),max_length=20, unique=True)
    release_date    = models.IntegerField(_('Release Year'), choices=YEAR_CHOICES)
    star_cast       = models.CharField(_('Movie Start Cast'), max_length=255, null=True, blank=True)
    rating          = models.FloatField(_('Movie Rating') , null=True, blank=True)
    votes           = models.CharField(_('Movie Votes'), max_length=100, null=True, blank=True)
    links           = models.CharField(_('Movie Detail Link'), max_length=100, blank=True, null=True)
    trailer         = models.CharField(_('Trailer Link'), max_length=200, null=True, blank=True)
    summary         = models.TextField(_('Movie Summary'), null=True, blank=True)
    img_source      = models.TextField(_('Image Short Image'), null=True, blank=True)
    taglines        = models.TextField(_('Movie TagLines'), blank=True, null=True)
    certificate     = models.CharField(_('Movie Certificate'), max_length=50, blank=True, null=True)
    trivia          = models.TextField(_('Movie Trivia'), blank=True, null=True)
    goofs           = models.TextField(_('Movie Goofs'), blank=True, null=True)
    country         = models.CharField(_('Movie Country'), max_length=100, blank=True, null=True)
    language        = models.CharField(_('Movie Language'), max_length=100, blank=True, null=True)
    budget          = models.CharField(_('Movie Total Budget'), max_length=50, blank=True, null=True)
    gross           = models.CharField(_('Movie Total Gross Amount'), max_length=50, null=True, blank=True)
    cumulative      = models.CharField(_('Movie Total Cumulative Amount'), max_length=50, null=True, blank=True)
    movie_dump      = models.TextField(_('Store more information here'), null=True, blank=True)
    created_at      = models.DateTimeField(_('Create At'), auto_now_add=True)
    updated_at      = models.DateTimeField(_('Update At'), auto_now=True)

    class Meta:
        verbose_name = _('movie')
        verbose_name_plural = _('movies')

    def get_avg_rating(self):
        """
        Convert float rating into readable format
        """
        return self.rating

    def __str__(self):
        return f'{self.title}'

    def last_updated(self):
        return self.updated_at


    def get_all(self):
        return self.objects.all()


WATCH_CHOICES = (
    ('watch_list', 'Watch List'),
    ('watched_list', 'Watched List')
)

class Watch(models.Model):
    user            = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    movie           = models.OneToOneField(Movie, on_delete=models.CASCADE)
    action          = models.CharField(max_length=20, choices=WATCH_CHOICES)

    class Meta:
        verbose_name        = _("watch/watched list")
        verbose_name_plural = _("watch/watched lists")
        unique_together     = (('user', 'movie'))

    def __str__(self):
        return '{} "added" <{}> to {}'.format(self.user.username.title(), self.movie.title, self.action)

    def get_watch_list(self, cls, user):
        return cls.object.filter(user=user, action='watch_list')

    def get_watched_list(self, user):
        return self.object.filter(user=user, action='watched_list')

