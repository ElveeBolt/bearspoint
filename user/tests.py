from django.test import TestCase
from django.test import Client
from service.models import Service
from master.models import Master, Calendar


# Create your tests here.
class ManagerTestCase(TestCase):
    client = Client()
    fixtures = ['fixtures/user.json', 'fixtures/master.json', 'fixtures/service.json']

    def test_service_post(self):
        self.client.login(username='admin', password='admin')
        response = self.client.post('/user/manager/services/add', {
            'title': 'Сервис',
            'description': 'Описание сервиса',
            'price': '300',
            'time': '60'
        })

        try:
            service = Service.objects.filter(title='Сервис')
        except Service.DoesNotExist:
            service = None

        self.assertIsNotNone(service)

    def test_service_delete(self):
        self.client.login(username='admin', password='admin')
        service = Service.objects.filter(title='Сервис 1').first()
        response = self.client.post(f'/user/manager/services/delete/{service.id}')

        try:
            service = Service.objects.filter(id=service.id)
        except Calendar.DoesNotExist:
            service = None

        self.assertIsNotNone(service)

    def test_master_post(self):
        self.client.login(username='admin', password='admin')
        response = self.client.post('/user/manager/masters/add', {
            'name': 'Мастер',
            'phone': '380506896320',
            'description': 'Описание мастера',
            'rang': '0',
            'status': '0',
            'service_1': '1'
        })
        try:
            master = Master.objects.filter(name='Мастер')
        except Master.DoesNotExist:
            master = None

        self.assertIsNotNone(master)

    def test_master_delete(self):
        self.client.login(username='admin', password='admin')
        master = Master.objects.filter(name='Мастер 1').first()
        response = self.client.post(f'/user/manager/masters/delete/{master.id}')

        try:
            master = Master.objects.filter(id=master.id)
        except Calendar.DoesNotExist:
            master = None

        self.assertIsNotNone(master)

    def test_calendar_post(self):
        self.client.login(username='admin', password='admin')
        response = self.client.post('/user/manager/calendars/add', {
            'master': 1,
            'date': '2020-12-14',
            'time_start': '08:00:00',
            'time_end': '17:00:00',
        })
        try:
            calendar = Calendar.objects.filter(date='2020-12-14')
        except Calendar.DoesNotExist:
            calendar = None

        self.assertIsNotNone(calendar)

    def test_calendar_delete(self):
        self.client.login(username='admin', password='admin')
        calendar = Calendar.objects.filter(date='2020-12-13').first()
        response = self.client.post(f'/user/manager/calendars/delete/{calendar.id}')

        try:
            calendar = Calendar.objects.filter(id=calendar.id)
        except Calendar.DoesNotExist:
            calendar = None

        self.assertIsNotNone(calendar)
