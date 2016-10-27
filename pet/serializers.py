from rest_framework import serializers
from .models import Pet, Breed, Birth


class PetSerializer(serializers.ModelSerializer):

    breed_id = serializers.PrimaryKeyRelatedField(
        source='breed', queryset=Breed.objects
    )
    father_id = serializers.PrimaryKeyRelatedField(
        source='birth.father', queryset=Pet.objects,
        default=None
    )
    mother_id = serializers.PrimaryKeyRelatedField(
        source='birth.mother', queryset=Pet.objects,
        default=None
    )
    owner = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta(object):
        model = Pet
        fields = [
            'id', 'created_at', 'updated_at',
            'breed_id', 'father_id', 'mother_id',
            'name', 'gender', 'owner',
        ]
        extra_kwargs = {
        }

    def create(self, validated_data):
        birth = validated_data.pop('birth')
        pet = super(PetSerializer, self).create(validated_data)
        Birth.objects.create(
            child=pet,
            mother=birth['mother'],
            father=birth['father']
        )
        return pet


class BreedSerializer(serializers.ModelSerializer):

    class Meta(object):
        model = Breed
        fields = ['name']


class BirthSerializer(serializers.ModelSerializer):

    class Meta(object):
        model = Birth
        exclude = []
