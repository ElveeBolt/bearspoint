from django.test import TestCase
from django.contrib.auth.models import User
from datetime import datetime, time
from .utils import convert_period_to_set, get_workday_master_time, calc_period
from .models import Booking
from master.models import Master, Calendar
from service.models import Service


# Create your tests here.
class ConvertPeriodToSetTestCase(TestCase):
    def test_convert_period_to_set(self):
        time_start = datetime(2023, 4, 6, 8, 0)
        time_end = datetime(2023, 4, 6, 9, 0)
        expected_result = {
            datetime(2023, 4, 6, 8, 0),
            datetime(2023, 4, 6, 8, 15),
            datetime(2023, 4, 6, 8, 30),
            datetime(2023, 4, 6, 8, 45),
            datetime(2023, 4, 6, 9, 0)
        }
        result = convert_period_to_set(time_start, time_end)
        self.assertSetEqual(result, expected_result)

    def test_string_convert_period_to_set(self):
        time_start = 'text'
        time_end = datetime(2023, 4, 6, 9, 0)
        with self.assertRaises(TypeError):
            convert_period_to_set(time_start, time_end)

    def test_reverse_convert_period_to_set(self):
        time_start = datetime(2023, 4, 6, 9, 0)
        time_end = datetime(2023, 4, 6, 8, 0)
        expected_result = set()
        result = convert_period_to_set(time_start, time_end)
        self.assertSetEqual(result, expected_result)

    def test_equals_convert_period_to_set(self):
        time_start = datetime(2023, 4, 6, 9, 0)
        time_end = datetime(2023, 4, 6, 9, 0)
        expected_result = {datetime(2023, 4, 6, 9, 0)}
        result = convert_period_to_set(time_start, time_end)
        self.assertSetEqual(result, expected_result)


class CalcPeriodTestCase(TestCase):
    def setUp(self):
        user = User.objects.create(username='user', password='password')

        service_1 = Service.objects.create(title='Сервис 1', description='text', price=300, time=60)
        service_2 = Service.objects.create(title='Сервис 2', description='text', price=300, time=30)

        master_1 = Master.objects.create(name='Мастер 1', phone=38050695200, description='text', rang=0, status=1)
        master_1.service.add(service_1)
        master_2 = Master.objects.create(name='Мастер 2', phone=38050333300, description='text', rang=0, status=1)
        master_2.service.add(service_1)
        master_3 = Master.objects.create(name='Мастер 3', phone=38050333322, description='text', rang=0, status=1)
        master_3.service.add(service_1, service_2)
        master_4 = Master.objects.create(name='Мастер 4', phone=38050695200, description='text', rang=0, status=0)
        master_4.service.add(service_1)

        Calendar.objects.create(master=master_1, date=datetime(2023, 4, 6), time_start=time(8, 0), time_end=time(10, 0))
        Calendar.objects.create(master=master_2, date=datetime(2023, 4, 6), time_start=time(8, 0), time_end=time(10, 0))
        Calendar.objects.create(master=master_3, date=datetime(2023, 4, 6), time_start=time(8, 0), time_end=time(10, 0))
        Calendar.objects.create(master=master_4, date=datetime(2023, 4, 6), time_start=time(8, 0), time_end=time(9, 15))

        Booking.objects.create(master=master_1, service=service_1, user=user, date=datetime(2023, 4, 6), time_start=time(8, 0))
        Booking.objects.create(master=master_3, service=service_2, user=user, date=datetime(2023, 4, 6), time_start=time(8, 30))
        Booking.objects.create(master=master_4, service=service_2, user=user, date=datetime(2023, 4, 6),time_start=time(8, 0))
        Booking.objects.create(master=master_4, service=service_2, user=user, date=datetime(2023, 4, 6), time_start=time(8, 45))

    def test_get_workday_master_time(self):
        master = Master.objects.get(name="Мастер 1")
        service = Service.objects.get(title="Сервис 1")
        calendar = Calendar.objects.get(master=master)
        expected_result = {
            datetime(2023, 4, 6, 8, 0),
            datetime(2023, 4, 6, 8, 15),
            datetime(2023, 4, 6, 8, 30),
            datetime(2023, 4, 6, 8, 45),
            datetime(2023, 4, 6, 9, 0)
        }
        result = get_workday_master_time(calendar, service)
        self.assertSetEqual(result, expected_result)

    def test_calc_period(self):
        """
        Test for the master if booking is empty
        """
        master = Master.objects.get(name="Мастер 2")
        service = Service.objects.get(title="Сервис 1")
        date = datetime(2023, 4, 6)
        expected_result = [time(8, 0), time(8, 15), time(8, 30), time(8, 45), time(9, 0)]
        result = calc_period(master, service, date)
        self.assertListEqual(result, expected_result)

    def test_booking_calc_period(self):
        """
        Test for the master if has 1 booking
        """
        master = Master.objects.get(name="Мастер 1")
        service = Service.objects.get(title="Сервис 1")
        date = datetime(2023, 4, 6)
        expected_result = [time(9, 0)]
        result = calc_period(master, service, date)
        self.assertListEqual(result, expected_result)

    def test_no_worktime_calc_period(self):
        """
        Test for the master who has a day off today
        """
        master = Master.objects.get(name="Мастер 1")
        service = Service.objects.get(title="Сервис 1")
        date = datetime(2023, 4, 7)
        expected_result = None
        result = calc_period(master, service, date)
        self.assertEquals(result, expected_result)

    def test_booking_between_calc_period(self):
        """
        Test for the master who has between booking
        """
        master = Master.objects.get(name="Мастер 3")
        service = Service.objects.get(title="Сервис 2")
        date = datetime(2023, 4, 6)
        expected_result = [time(8, 0), time(9, 0), time(9, 15), time(9, 30)]
        result = calc_period(master, service, date)
        self.assertListEqual(result, expected_result)

    def test_booking_full_calc_period(self):
        """
        Test for the master who has between booking
        """
        master = Master.objects.get(name="Мастер 4")
        service = Service.objects.get(title="Сервис 2")
        date = datetime(2023, 4, 6)
        expected_result = []
        result = calc_period(master, service, date)
        self.assertListEqual(result, expected_result)