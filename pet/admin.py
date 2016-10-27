# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Breed, Pet, Birth


class BreedAdmin(admin.ModelAdmin):
    list_display = ['name']


class PetAdmin(admin.ModelAdmin):
    list_display = ['name', 'birth']


class BirthAdmin(admin.ModelAdmin):
    list_display = ['child', 'father', 'mother']


admin.site.register(Breed, BreedAdmin)
admin.site.register(Pet, PetAdmin)
admin.site.register(Birth, BirthAdmin)
