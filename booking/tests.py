from django.test import TestCase
from datetime import datetime, time
from .utils import convert_period_to_set, get_workday_master_time, calc_period
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
    fixtures = ['fixtures/user.json', 'fixtures/master.json', 'fixtures/service.json', 'fixtures/booking.json']

    def test_get_workday_master_time(self):
        master = Master.objects.get(name="Мастер 1")
        service = Service.objects.get(title="Сервис 1")
        calendar = Calendar.objects.get(master=master, date="2023-04-06")
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