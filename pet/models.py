# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings


class EditTimeTrackable(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta(object):
        abstract = True


class Namable(models.Model):
    name = models.CharField(unique=True, max_length=255)

    class Meta(object):
        abstract = True


class Breed(EditTimeTrackable, Namable):
    """Class is a model that keep pet bread."""


class Pet(Namable, EditTimeTrackable):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL)
    breed = models.ForeignKey(Breed)

    GENDERS = (
        ('male', 'male'),
        ('female', 'female'),
    )
    gender = models.CharField(choices=GENDERS, max_length=6)


class Birth(EditTimeTrackable):
    child = models.OneToOneField(Pet)
    father = models.ForeignKey(Pet, related_name='father_of')
    mother = models.ForeignKey(Pet, related_name='mother_of')
