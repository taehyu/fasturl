from django.test import TestCase

# Create your tests here.
from rest_framework import status
from rest_framework.test import APITestCase


class UrlViewTestTestCase(APITestCase):
    def setUp(self) -> None:
        pass

    def test_shorten_url(self):
        data = {'url': 'www.google.com'}
        response = self.client.post('/api/urls/shorten', data=data)
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['url'], data['url'])
        self.fail()
