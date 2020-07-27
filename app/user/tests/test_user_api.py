from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status


CREATE_USER_URL = reverse('user:create')

def create_user(**params):
    return get_user_model().objects.create_user(**params)




class PublicUserApiTests(TestCase):

    def setUp(self):
        self.client = APIClient()


    def test_(self):
        payload = {'email': 'test@pass.com', 'password': '123Test', 'name': 'test name'}
        response = self.client.post(CREATE_USER_URL, payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        user = get_user_model().objects.get(**response.data)
        self.assertNotIn('password', response.data)


    # def test_(self):
    # def test_(self):
    # def test_(self):
    # def test_(self):
