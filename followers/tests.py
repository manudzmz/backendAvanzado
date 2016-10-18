from django.contrib.auth.models import User
from django.test import TestCase

# Create your tests here.
from followers.models import Relationship
from followers.utils import get_followers


class RelationshipTests(TestCase):
    def test_get_followers_returns_users_that_follow_a_given_user(self):
        user1 = User.objects.create_user('luke', 'skywalker@starwars.com', "skywalker")
        user2 = User.objects.create_user('anakin', 'annie@starwars.com', 'skywalker')

        Relationship.objects.create(origin=user1, target=user2)  # user1 sigue a user2

        followers = get_followers(user2)

        self.assertEqual([user1], followers)  # followers == [user1]
