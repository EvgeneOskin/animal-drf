# -*- coding: utf-8 -*-
from factory import DjangoModelFactory, Faker, fuzzy, SubFactory, Iterator
from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase, RequestsClient
from requests.auth import HTTPBasicAuth
from .models import Pet, Birth, Breed


class UserFactory(DjangoModelFactory):

    class Meta(object):
        model = get_user_model()

    username = Faker('name')

    @classmethod
    def _prepare(cls, create, **kwargs):
        password = kwargs.pop('password', None)
        user = super(UserFactory, cls)._prepare(create, **kwargs)
        if password:
            user.set_password(password)
            if create:
                user.save()
        return user


class BreedFactory(DjangoModelFactory):

    class Meta(object):
        model = Breed


class PetFactory(DjangoModelFactory):

    class Meta(object):
        model = Pet

    name = fuzzy.FuzzyText('')
    gender = fuzzy.FuzzyChoice(['male', 'female'])
    breed = Iterator(Breed.objects.all())
    owner = SubFactory(UserFactory)


class BirthFactory(DjangoModelFactory):

    class Meta(object):
        model = Birth


    child = SubFactory(PetFactory)
    father = SubFactory(PetFactory, gender='male')
    mother = SubFactory(PetFactory, gender='female')


class PetTest(APITestCase):

    url = 'https://testserver/api/v1/pet/'

    client_class = RequestsClient

    def setUp(self):
        self.pets = PetFactory.create_batch(10)
        password = 'password'
        user = UserFactory(password=password)
        self.client.auth = HTTPBasicAuth(user.username, password)

    @classmethod
    def setUpTestData(cls):
        cls.breed = BreedFactory(name='dog')

    def test_list(self):
        response = self.client.get('https://testserver/api/v1/pet/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), len(self.pets))
        pet_json = response.json()[0]
        pet = Pet.objects.get(pk=pet_json['id'])
        self.assertEqual(pet_json, {
            'id': pet.id,
            'breed_id': pet.breed.pk,
            'name': pet.name,
            'father_id': None,
            'mother_id': None,
            'name': pet.name,
            'gender': pet.gender,
            'created_at': pet.created_at.replace(tzinfo=None).isoformat() + 'Z',
            'updated_at': pet.updated_at.replace(tzinfo=None).isoformat() + 'Z',
        })

    def test_create_with_parent(self):
        new_pet = {
            'name': 'excavata',
            'breed_id': self.breed.pk,
            'gender': 'male'
        }
        response = self.client.post(self.url, json=new_pet)
        self.assertEqual(response.status_code, 201)
        pet_json = response.json()
        pet = Pet.objects.get(pk=pet_json['id'])
        self.assertEqual(pet_json, {
            'id': pet.id,
            'breed_id': pet.breed.pk,
            'name': pet.name,
            'father_id': None,
            'mother_id': None,
            'name': pet.name,
            'gender': pet.gender,
            'created_at': pet.created_at.replace(tzinfo=None).isoformat() + 'Z',
            'updated_at': pet.updated_at.replace(tzinfo=None).isoformat() + 'Z',
        })


class UnauthenticatedTest(APITestCase):

    def test_list_pet(self):
        for i in ('pet', 'birth', 'breed'):
            response = self.client.get('/api/v1/{}/'.format(i))
            self.assertEqual(response.status_code, 401)
