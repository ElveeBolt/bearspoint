from django.views.generic import DetailView, ListView
from .models import Service


# Create your views here.
class ServiceListView(ListView):
    model = Service
    template_name = 'service/service_list.html'
    context_object_name = 'service_list'
    extra_context = {
        'title': 'Услуги',
        'subtitle': 'Lorem Ipsum'
    }


class ServiceDetailView(DetailView):
    model = Service
    template_name = 'service/service.html'
    extra_context = {
        'title': 'Услуга',
        'subtitle': 'Lorem Ipsum'
    }
