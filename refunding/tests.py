import datetime

from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse


class DateInFormsTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.username = 'testuser'
        cls.password = 'djangooo'

        cls.user = User.objects.create_superuser(username=cls.username, email='', password=cls.password)

    def test_refund_date_appears_at_creation(self):
        c = Client()
        c.login(username=self.username, password=self.password)
        response = c.get(reverse('new_refund'))
        self.assertLess(response.status_code, 300)

        expected_date = datetime.date.today().isoformat()
        self.assertIn(expected_date,response.content.decode('utf-8'))

