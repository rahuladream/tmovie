# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Django Imports
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.base_user import BaseUserManager

# Local imports here

class TimestampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class UserManager(BaseUserManager):
    use_in_migration = True

    def _create_user(self, email, password, **extra_fields):
        
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        now = timezone.now()
        user = self.model(
            email = email,
            last_login = now,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_user(self, email, password, **extra_fields):
        return self._create_user(email, password, **extra_fields)
    
    def create_superuser(self, email, password, **extra_fields):
        user = self._create_user(email, password, **extra_fields)
        return user

USER_ROLE = (('ADMIN', 'ADMIN'),
        ('USER', 'USER')
        )

class User(AbstractBaseUser, PermissionMixin):
    username = models.CharField(max_length=80, blank=True)
    email = models.EmailField(_("Email address"), unique=True)
    first_name = models.CharField(('First Name'), max_length=30, blank=True)
    last_name = models.CharField(('Last Name'), max_length=30, blank=True)
    role = models.CharField(max_length=20, choices=USER_ROLE)

    objects = UserManager()

    USERNAME_FIELD = 'email'

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