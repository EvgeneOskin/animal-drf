# -*- coding: utf-8 -*-
from rest_framework import viewsets, mixins
from .models import Pet, Birth, Breed
from .serializers import PetSerializer, BreedSerializer, BirthSerializer


class PetViewSet(mixins.CreateModelMixin,
                 mixins.ListModelMixin,
                 viewsets.GenericViewSet):

    queryset = Pet.objects
    serializer_class = PetSerializer


class BirthViewSet(mixins.ListModelMixin,
                   viewsets.GenericViewSet):

    queryset = Birth.objects
    serializer_class = BirthSerializer


class BreedViewSet(mixins.ListModelMixin,
                   viewsets.GenericViewSet):

    queryset = Breed.objects
    serializer_class = BreedSerializer
