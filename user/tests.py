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
        }, follow=True)
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
        }, follow=True)
        master = Master.objects.filter(name='Мастер 1')
        self.assertEquals(len(master), 1)

