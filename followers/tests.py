from django.contrib.auth.models import User
from django.test import TestCase

# Create your tests here.
from django.test import override_settings
from rest_framework.test import APITestCase
from rest_framework import status

from followers.models import Relationship
from followers.utils import get_followers, get_following


class RelationshipTests(TestCase):
    def setUp(self):
        """
        Se ejecuta antes de cada test
        """
        self.user1 = User.objects.create_user('luke', 'skywalker@starwars.com', "skywalker")
        self.user2 = User.objects.create_user('anakin', 'annie@starwars.com', 'skywalker')
        Relationship.objects.create(origin=self.user1, target=self.user2)  # user1 sigue a user2

    def test_get_followers_returns_users_that_follow_a_given_user(self):
        followers = get_followers(self.user2)
        self.assertEqual([self.user1], followers)  # followers == [user1]

    def test_get_following_returns_users_followed_by_a_given_user(self):
        following = get_following(self.user1)
        self.assertEqual([self.user2], following)  # following == [user2]


@override_settings(ROOT_URLCONF='followers.urls')
class APITests(APITestCase):

    USERS_PASSWORD = "skywalker"
    FOLLOWING_API_URL = '/following/'

    def setUp(self):
        # preparar el juego de datos
        self.user1 = User.objects.create_user('luke', 'skywalker@starwars.com', self.USERS_PASSWORD)
        self.user2 = User.objects.create_user('anakin', 'annie@starwars.com', self.USERS_PASSWORD)
        self.user3 = User.objects.create_user('chewe', 'chewe@starwars.com', self.USERS_PASSWORD)
        self.user4 = User.objects.create_user('han', 'solo@starwars.com', self.USERS_PASSWORD)
        self.user5 = User.objects.create_user('r2d2', 'r2d2@starwars.com', self.USERS_PASSWORD)
        self.user6 = User.objects.create_user('c3po', 'c3po@starwars.com', self.USERS_PASSWORD)
        self.user7 = User.objects.create_user('leia', 'leia@starwars.com', self.USERS_PASSWORD)
        self.user8 = User.objects.create_user('finn', 'finn@starwars.com', self.USERS_PASSWORD)

        # Relaciones del user1
        Relationship.objects.create(origin=self.user1, target=self.user2)  # user1 sigue a user2
        Relationship.objects.create(origin=self.user1, target=self.user3)  # user1 sigue a user3
        Relationship.objects.create(origin=self.user1, target=self.user4)  # user1 sigue a user4
        Relationship.objects.create(origin=self.user1, target=self.user5)  # user1 sigue a user5
        Relationship.objects.create(origin=self.user1, target=self.user6)  # user1 sigue a user6
        Relationship.objects.create(origin=self.user1, target=self.user7)  # user1 sigue a user7
        Relationship.objects.create(origin=self.user1, target=self.user8)  # user1 sigue a user8

        # Relaciones del user3
        Relationship.objects.create(origin=self.user3, target=self.user1)  # user3 sigue a user1
        Relationship.objects.create(origin=self.user3, target=self.user2)  # user3 sigue a user2
        Relationship.objects.create(origin=self.user3, target=self.user4)  # user3 sigue a user4

    def test_following_users_endpoint_fails_when_user_is_not_authenticated(self):
        Relationship.objects.create(origin=self.user1, target=self.user2)  # user1 sigue a user2

        # hacer peticion
        response = self.client.get(self.FOLLOWING_API_URL)

        # asegurarmos que la respuesta es un codigo 403
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_user_doesnt_follow_any_user_and_empty_list_is_returned(self):
        # autenticar al user2
        self.client.login(username=self.user2.username, password=self.USERS_PASSWORD)

        # hacer peticion
        response = self.client.get(self.FOLLOWING_API_URL)

        # aseguramos que la respuesta es un codigo 200
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # aseguramos que la longitud de los datos devueltos es cero
        self.assertEqual(len(response.data), 0)

    def test_user_follows_three_users_and_three_users_are_returned(self):
        # autenticar al user1
        self.client.login(username=self.user3.username, password=self.USERS_PASSWORD)

        # hacer peticion
        response = self.client.get(self.FOLLOWING_API_URL)

        # aseguramos que la respuesta es un codigo 200
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # aseguramos que la longitud de los datos devueltos es tres
        self.assertEqual(len(response.data), 3)


    def test_user_follows_seven_users_and_seven_users_are_returned(self):
        # autenticar al user1
        self.client.login(username=self.user1.username, password=self.USERS_PASSWORD)

        # hacer peticion
        response = self.client.get(self.FOLLOWING_API_URL)

        # aseguramos que la respuesta es un codigo 200
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # aseguramos que la longitud de los datos devueltos es tres
        self.assertEqual(len(response.data), 7)