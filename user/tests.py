from django.test import TestCase
from django.test import Client
from django.contrib.auth.models import User
from service.models import Service
from master.models import Master, Calendar


# Create your tests here.
class ManagerTestCase(TestCase):
    client = Client()

    def setUp(self):
        # Create user
        user = User.objects.create(username='admin')
        user.set_password('admin')
        user.save()

    def test_service_post(self):
        self.client.login(username='admin', password='admin')
        response = self.client.post('/user/manager/services/add', {
            'title': 'Сервис 1',
            'description': 'Описание сервиса',
            'price': '300',
            'time': '60'
        })
        service = Service.objects.filter(title='Сервис 1')
        self.assertEquals(len(service), 1)

    def test_master_post(self):
        self.client.login(username='admin', password='admin')
        response = self.client.post('/user/manager/masters/add', {
            'name': 'Мастер 1',
            'phone': '380506896320',
            'description': 'Описание мастера',
            'rang': '0',
            'status': '0',
            'service_1': '1'
        })
        master = Master.objects.filter(name='Мастер 1')
        self.assertEquals(len(master), 1)


    def test_calendar_post(self):
        self.client.login(username='admin', password='admin')
        master = Master.objects.create(name='Мастер 4', phone=38050695200, description='text', rang=0, status=1)
        response = self.client.post('/user/manager/calendars/add', {
            'master': master.id,
            'date': '2020-12-12',
            'time_start': '08:00',
            'time_end': '17:00',
        })
        calendar = Calendar.objects.all()
        self.assertEquals(len(calendar), 1)

