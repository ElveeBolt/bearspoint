from django.test import TestCase
from django.test import Client
from django.contrib.auth.models import User
from master.models import Master
from service.models import Service
from booking.models import Booking


# Create your tests here.
class BookingTestCase(TestCase):
    client = Client()

    def setUp(self):
        user = User.objects.create(username='user')
        user.set_password('password')
        user.save()

    def test_booking(self):
        user = self.client.login(username='user', password='password')
        service = Service.objects.create(title='Сервис 1', description='text', price=300, time=60)
        master = Master.objects.create(name='Мастер 1', phone=38050695200, description='text', rang=0, status=1)
        master.service.add(service)

        response = self.client.post(f'/services/{service.id}', {
            'master': master.id,
            'user': user,
            'service': service.id,
            'date': '2020-12-12',
            'time_start': '08:00',
        })

        booking = Booking.objects.filter(master=master.id)
        self.assertEquals(len(booking), 1)
