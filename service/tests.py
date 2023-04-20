from django.test import TestCase
from django.test import Client
from booking.models import Booking


# Create your tests here.
class BookingTestCase(TestCase):
    client = Client()
    fixtures = ['fixtures/user.json', 'fixtures/master.json', 'fixtures/service.json']

    def test_booking(self):
        user = self.client.login(username='admin', password='admin')

        response = self.client.post('/services/1', {
            'master': 1,
            'user': user,
            'service': 1,
            'date': '2020-12-12',
            'time_start': '08:00',
        })

        try:
            booking = Booking.objects.filter(master=1, user=user)
        except Booking.DoesNotExist:
            booking = None

        self.assertIsNotNone(booking)
