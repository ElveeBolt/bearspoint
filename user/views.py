from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.conf import settings
from django.views.generic import TemplateView, ListView, UpdateView, DeleteView, CreateView
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from user.mixins import UserCheckAdministratorMixin
from master.models import Master, Calendar
from master.forms import MasterForm, CalendarForm
from service.forms import ServiceForm
from service.models import Service
from booking.models import Booking
from booking.forms import BookingForm
from user.forms import SignupForm
from .forms import LoginForm


# Create your views here.
class UserView(TemplateView):
    template_name = 'user/index.html'
    extra_context = {
        'title': 'Пользователь',
        'subtitle': 'Lorem'
    }


class ManagerMasterListView(LoginRequiredMixin, UserCheckAdministratorMixin, ListView):
    model = Master
    template_name = 'user/manager/masters.html'
    context_object_name = 'master_list'
    extra_context = {
        'title': 'Мастера',
        'subtitle': 'Управление мастерами'
    }


class ManagerMasterUpdateView(LoginRequiredMixin, UserCheckAdministratorMixin, UpdateView):
    model = Master
    form_class = MasterForm
    template_name = 'user/manager/master.html'
    context_object_name = 'master'
    extra_context = {
        'title': 'Редактирование мастера',
        'subtitle': 'Внесение изменений к мастеру'
    }


class ManagerMasterCreateView(LoginRequiredMixin, UserCheckAdministratorMixin, CreateView):
    model = Master
    form_class = MasterForm
    template_name = 'user/manager/master.html'
    extra_context = {
        'title': 'Добавление мастера',
        'subtitle': 'Добавление нового мастера',
    }


class ManagerMasterDeleteView(LoginRequiredMixin, UserCheckAdministratorMixin, DeleteView):
    model = Master
    success_url = "/user/manager/masters"


class ManagerCalendarListView(LoginRequiredMixin, UserCheckAdministratorMixin, ListView):
    model = Calendar
    template_name = 'user/manager/calendars.html'
    context_object_name = 'calendar_list'
    extra_context = {
        'title': 'Графики работы',
        'subtitle': 'Управление графиками работы мастеров салона'
    }


class ManagerCalendarUpdateView(LoginRequiredMixin, UserCheckAdministratorMixin, UpdateView):
    model = Calendar
    form_class = CalendarForm
    template_name = 'user/manager/calendar.html'
    context_object_name = 'calendar'
    extra_context = {
        'title': 'Редактирование мастера',
        'subtitle': 'Внесение изменений к мастеру'
    }


class ManagerCalendarCreateView(LoginRequiredMixin, UserCheckAdministratorMixin, CreateView):
    model = Calendar
    form_class = CalendarForm
    template_name = 'user/manager/calendar.html'
    extra_context = {
        'title': 'Новый график работы',
        'subtitle': 'Добавление графика работы',
    }


class ManagerCalendarDeleteView(LoginRequiredMixin, UserCheckAdministratorMixin, DeleteView):
    model = Calendar
    success_url = "/user/manager/calendars"


class ManagerServiceListView(LoginRequiredMixin, UserCheckAdministratorMixin, ListView):
    model = Service
    template_name = 'user/manager/services.html'
    context_object_name = 'service_list'
    extra_context = {
        'title': 'Услуги',
        'subtitle': 'Управление услугами салона'
    }


class ManagerServiceUpdateView(LoginRequiredMixin, UserCheckAdministratorMixin, UpdateView):
    model = Service
    form_class = ServiceForm
    template_name = 'user/manager/service.html'
    context_object_name = 'service'
    extra_context = {
        'title': 'Редактирование услуги',
        'subtitle': 'Внесение изменений в услугу'
    }


class ManagerServiceCreateView(LoginRequiredMixin, UserCheckAdministratorMixin, CreateView):
    model = Service
    form_class = ServiceForm
    template_name = 'user/manager/service.html'
    extra_context = {
        'title': 'Новая услуга',
        'subtitle': 'Добавление новой услуги',
    }


class ManagerServiceDeleteView(LoginRequiredMixin, UserCheckAdministratorMixin, DeleteView):
    model = Service
    success_url = "/user/manager/services"


class ManagerBookingListView(LoginRequiredMixin, UserCheckAdministratorMixin, ListView):
    model = Booking
    template_name = 'user/manager/bookings.html'
    context_object_name = 'booking_list'
    extra_context = {
        'title': 'Бронирования',
        'subtitle': 'Управление бронированиями салона'
    }


class ManagerBookingUpdateView(LoginRequiredMixin, UserCheckAdministratorMixin, UpdateView):
    model = Booking
    form_class = BookingForm
    template_name = 'user/manager/booking.html'
    context_object_name = 'service'
    extra_context = {
        'title': 'Редактирование бронирования',
        'subtitle': 'Внесение изменений в бронирование'
    }


class ManagerBookingCreateView(LoginRequiredMixin, UserCheckAdministratorMixin, CreateView):
    model = Booking
    form_class = BookingForm
    template_name = 'user/manager/booking.html'
    extra_context = {
        'title': 'Новое бронирование',
        'subtitle': 'Добавления нового бронирования',
    }


class ManagerBookingDeleteView(LoginRequiredMixin, UserCheckAdministratorMixin, DeleteView):
    model = Booking
    success_url = "/user/manager/bookings"


class UserLoginView(LoginView):
    form_class = LoginForm
    template_name = 'user/login.html'
    success_url = reverse_lazy('user/manager')
    redirect_authenticated_user = True
    extra_context = {
        'title': 'Авторизация',
        'subtitle': 'Для того, чтобы использовать сервис выполните авторизацию',
    }


class UserSignupView(CreateView):
    model = User
    form_class = SignupForm
    template_name = 'user/signup.html'
    success_url = reverse_lazy('login')
    extra_context = {
        'title': 'Регистрация профиля',
        'subtitle': 'Создайте профиль для того, чтобы использовать BearsPoint',
    }

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('user')
        else:
            return super().dispatch(request, *args, **kwargs)


class UserLogoutView(LogoutView):
    next_page = settings.LOGOUT_REDIRECT_URL
