from datetime import datetime

from django.test import TestCase

from eventex.subscriptions.models import Subscription


class SubscriptionModelTest(TestCase):

    def setUp(self):
        self.obj = Subscription(
            name='Eric Vieira',
            cpf='12345678901',
            email='eric.vieira@me.com',
            phone='21-99889-3320'
        )
        self.obj.save()

    def test_create(self):
        self.assertTrue(Subscription.objects.exists())

    def test_created_at(self):
        """Subscription must have an a auto created_at attr. """
        self.assertIsInstance(self.obj.created_at, datetime)

    def test_str(self):
        self.assertEqual('Eric Vieira', str(self.obj))


    def test_paid_default_to_False(self):
        """By default paid must be false"""
        self.assertEqual(False, self.obj.paid)
