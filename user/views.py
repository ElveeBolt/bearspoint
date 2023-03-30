from django.views.generic import TemplateView, ListView, UpdateView, DeleteView, CreateView
from master.models import Master
from master.forms import MasterForm
from service.forms import ServiceForm
from service.models import Service


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
        'title': 'Управление мастерами',
        'subtitle': 'Lorem'
    }


class ManagerMasterUpdateView(UpdateView):
    model = Master
    form_class = MasterForm
    template_name = 'user/manager/master.html'
    context_object_name = 'master'
    extra_context = {
        'title': 'Редактирование мастера',
        'subtitle': 'Lorem'
    }


class ManagerMasterCreateView(CreateView):
    model = Master
    form_class = MasterForm
    template_name = 'user/manager/master.html'
    extra_context = {
        'title': 'Добавление мастера',
        'subtitle': 'Lorem',
    }


class ManagerMasterDeleteView(DeleteView):
    model = Master
    success_url = "/user/manager/masters"


class ManagerServiceListView(ListView):
    model = Service
    template_name = 'user/manager/services.html'
    context_object_name = 'service_list'
    extra_context = {
        'title': 'Управление услугами',
        'subtitle': 'Lorem'
    }


class ManagerServiceUpdateView(UpdateView):
    model = Service
    form_class = ServiceForm
    template_name = 'user/manager/service.html'
    context_object_name = 'service'
    extra_context = {
        'title': 'Редактирование услуги',
        'subtitle': 'Lorem'
    }


class ManagerServiceCreateView(CreateView):
    model = Service
    form_class = ServiceForm
    template_name = 'user/manager/service.html'
    extra_context = {
        'title': 'Добавление услуги',
        'subtitle': 'Lorem',
    }


class ManagerServiceDeleteView(DeleteView):
    model = Service
    success_url = "/user/manager/services"
