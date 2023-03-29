from django.views.generic import TemplateView, ListView, UpdateView, DeleteView
from master.models import Master
from master.forms import MasterForm


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


class ManagerMasterDeleteView(DeleteView):
    model = Master
    success_url = "/user/manager/masters"
