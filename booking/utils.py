from datetime import timedelta, datetime
from booking.models import Booking
from master.models import Calendar


def convert_period_to_set(time_start, time_end):
    time_set = set()
    while time_start <= time_end:
        time_set.add(time_start)
        time_start += timedelta(minutes=15)

    return time_set


def get_busy_booking_time(bookings):
    busy_time = []

    for booking in bookings:
        time_start = datetime.combine(booking.date, booking.time_start)
        time_end = time_start + timedelta(minutes=booking.service.time)

        busy_time.append(convert_period_to_set(time_start, time_end))
    return busy_time


def get_workday_master_time(calendar, service):
    time_start = datetime.combine(calendar.date, calendar.time_start)
    time_end = datetime.combine(calendar.date, calendar.time_end) - timedelta(minutes=service.time)
    return convert_period_to_set(time_start, time_end)


def calc_period(master, service, date) -> list or None:
    free_time = []

    try:
        calendar = Calendar.objects.get(master=master, date=date)
        work_times = get_workday_master_time(calendar, service)
    except Calendar.DoesNotExist:
        return

    bookings = Booking.objects.filter(master=master, date=date)
    busy_time = get_busy_booking_time(bookings)

    for time_start in work_times:
        possible_time = convert_period_to_set(time_start, time_start + timedelta(minutes=service.time))

        no_intersection = True
        for one_booking in busy_time:
            if len(possible_time.intersection(one_booking)) > 1:
                no_intersection = False
                break

        if no_intersection:
            free_time.append(time_start.time())

    return sorted(free_time)
