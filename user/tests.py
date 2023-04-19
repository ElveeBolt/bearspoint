from datetime import datetime, time
from django.test import TestCase
from django.test import Client
from django.contrib.auth.models import User, Group
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

        # Create group
        group = Group.objects.create(name='administrator')
        group.save()

        # Add group to user
        user.groups.add(group)
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
        print(service)
        self.assertEquals(len(service), 1)

    def test_service_delete(self):
        self.client.login(username='admin', password='admin')
        service = Service.objects.create(title='Сервис 1', description='text', price=300, time=60)
        response = self.client.post(f'/user/manager/services/delete/{service.id}')
        service = Service.objects.all()
        self.assertEquals(len(service), 0)

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

    def test_master_delete(self):
        self.client.login(username='admin', password='admin')
        master = Master.objects.create(name='Мастер 1', phone=38050695200, description='text', rang=0, status=1)
        response = self.client.post(f'/user/manager/masters/delete/{master.id}')
        master = Master.objects.all()
        self.assertEquals(len(master), 0)

    def test_calendar_post(self):
        self.client.login(username='admin', password='admin')
        master = Master.objects.create(name='Мастер 4', phone=38050695200, description='text', rang=0, status=1)
        response = self.client.post('/user/manager/calendars/add', {
            'master': master.id,
            'date': '2020-12-12',
            'time_start': '08:00',
            'time_end': '17:00',
        })
        calendar = Calendar.objects.filter(master=master.id)
        self.assertEquals(len(calendar), 1)

    def test_calendar_delete(self):
        self.client.login(username='admin', password='admin')
        master = Master.objects.create(name='Мастер 1', phone=38050695200, description='text', rang=0, status=1)
        calendar = Calendar.objects.create(master=master, date=datetime(2023, 4, 6), time_start=time(8, 0), time_end=time(10, 0))
        response = self.client.post(f'/user/manager/calendars/delete/{calendar.id}')
        calendar = Calendar.objects.all()
        self.assertEquals(len(calendar), 0)

