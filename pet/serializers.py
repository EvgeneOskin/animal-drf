from rest_framework import serializers
from .models import Pet, Breed, Birth


class PetSerializer(serializers.ModelSerializer):

    breed_id = serializers.PrimaryKeyRelatedField(
        source='breed', queryset=Breed.objects
    )
    father_id = serializers.PrimaryKeyRelatedField(
        source='birth.father', read_only=True
    )
    mother_id = serializers.PrimaryKeyRelatedField(
        source='birth.mother', read_only=True
    )

    class Meta(object):
        model = Pet
        fields = [
            'id', 'created_at', 'updated_at',
            'breed_id', 'father_id', 'mother_id',
            'name'
        ]


class BreedSerializer(serializers.ModelSerializer):

    class Meta(object):
        model = Breed
        exclude = []


class BirthSerializer(serializers.ModelSerializer):

    class Meta(object):
        model = Birth
        exclude = []
