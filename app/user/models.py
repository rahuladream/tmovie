# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Django Imports
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

# Local imports here

class TimestampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


USER_ROLE = (('ADMIN', 'ADMIN'),
        ('USER', 'USER')
        )

class CustomeUser(AbstractUser, TimestampModel):
    first_name = models.CharField(('First Name'), max_length=30, blank=True)
    last_name = models.CharField(('Last Name'), max_length=30, blank=True)
    role = models.CharField(max_length=20, choices=USER_ROLE)

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
    
    def get_full_name(self):
        """
        Return first_name + last_name with space
        """
        full_name = '{} {}'.format(self.first_name, self.last_name)
        return full_name.strip()
    
    def get_short_name(self):
        return self.first_name
    
    def __unicode__(self):
        return self.email