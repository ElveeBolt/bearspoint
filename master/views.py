from django.views.generic import DetailView, ListView
from .models import Master


# Create your views here.
class MasterListView(ListView):
    model = Master
    template_name = 'master/master_list.html'
    context_object_name = 'master_list'
    extra_context = {
        'title': 'Мастера',
        'subtitle': 'Список наших мастеров'
    }


class MasterDetailView(DetailView):
    model = Master
    template_name = 'master/master.html'
    extra_context = {
        'title': 'Мастер',
        'subtitle': 'Lorem Ipsum'
    }
