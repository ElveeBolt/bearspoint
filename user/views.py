from django.views.generic import TemplateView, ListView, UpdateView, DeleteView, CreateView
from master.models import Master, Calendar
from master.forms import MasterForm, CalendarForm
from service.forms import ServiceForm
from service.models import Service
from booking.models import Booking
from booking.forms import BookingForm


# Create your views here.
class UserView(TemplateView):
    template_name = 'user/index.html'
    extra_context = {
        'title': 'Пользователь',
        'subtitle': 'Lorem'
    }


class ManagerMasterListView(ListView):
    model = Master
    template_name = 'user/manager/masters.html'
    context_object_name = 'master_list'
    extra_context = {
        'title': 'Мастера',
        'subtitle': 'Управление мастерами'
    }


class ManagerMasterUpdateView(UpdateView):
    model = Master
    form_class = MasterForm
    template_name = 'user/manager/master.html'
    context_object_name = 'master'
    extra_context = {
        'title': 'Редактирование мастера',
        'subtitle': 'Внесение изменений к мастеру'
    }


class ManagerMasterCreateView(CreateView):
    model = Master
    form_class = MasterForm
    template_name = 'user/manager/master.html'
    extra_context = {
        'title': 'Добавление мастера',
        'subtitle': 'Добавление нового мастера',
    }


class ManagerMasterDeleteView(DeleteView):
    model = Master
    success_url = "/user/manager/masters"


class ManagerCalendarListView(ListView):
    model = Calendar
    template_name = 'user/manager/calendars.html'
    context_object_name = 'calendar_list'
    extra_context = {
        'title': 'Графики работы',
        'subtitle': 'Управление графиками работы мастеров салона'
    }


class ManagerCalendarUpdateView(UpdateView):
    model = Calendar
    form_class = CalendarForm
    template_name = 'user/manager/calendar.html'
    context_object_name = 'calendar'
    extra_context = {
        'title': 'Редактирование мастера',
        'subtitle': 'Внесение изменений к мастеру'
    }


class ManagerCalendarCreateView(CreateView):
    model = Calendar
    form_class = CalendarForm
    template_name = 'user/manager/calendar.html'
    extra_context = {
        'title': 'Новый график работы',
        'subtitle': 'Добавление графика работы',
    }


class ManagerCalendarDeleteView(DeleteView):
    model = Calendar
    success_url = "/user/manager/calendars"


class ManagerServiceListView(ListView):
    model = Service
    template_name = 'user/manager/services.html'
    context_object_name = 'service_list'
    extra_context = {
        'title': 'Услуги',
        'subtitle': 'Управление услугами салона'
    }


class ManagerServiceUpdateView(UpdateView):
    model = Service
    form_class = ServiceForm
    template_name = 'user/manager/service.html'
    context_object_name = 'service'
    extra_context = {
        'title': 'Редактирование услуги',
        'subtitle': 'Внесение изменений в услугу'
    }


class ManagerServiceCreateView(CreateView):
    model = Service
    form_class = ServiceForm
    template_name = 'user/manager/service.html'
    extra_context = {
        'title': 'Новая услуга',
        'subtitle': 'Добавление новой услуги',
    }


class ManagerServiceDeleteView(DeleteView):
    model = Service
    success_url = "/user/manager/services"


class ManagerBookingListView(ListView):
    model = Booking
    template_name = 'user/manager/bookings.html'
    context_object_name = 'booking_list'
    extra_context = {
        'title': 'Управление бронированиями',
        'subtitle': 'Lorem'
    }


class ManagerBookingUpdateView(UpdateView):
    model = Booking
    form_class = BookingForm
    template_name = 'user/manager/booking.html'
    context_object_name = 'service'
    extra_context = {
        'title': 'Редактирование бронирования',
        'subtitle': 'Lorem'
    }


class ManagerBookingCreateView(CreateView):
    model = Booking
    form_class = BookingForm
    template_name = 'user/manager/booking.html'
    extra_context = {
        'title': 'Добавление бронирования',
        'subtitle': 'Lorem',
    }


class ManagerBookingDeleteView(DeleteView):
    model = Booking
    success_url = "/user/manager/bookings"
