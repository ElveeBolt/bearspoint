import datetime
from django.views.generic import DetailView, ListView
from .models import Service
from master.models import Master, Calendar


# Create your views here.
class ServiceListView(ListView):
    model = Service
    template_name = 'service/service_list.html'
    context_object_name = 'service_list'
    extra_context = {
        'title': 'Услуги',
        'subtitle': 'Lorem Ipsum'
    }

    # def get_queryset(self):
    #     master_calendar = super().get_queryset().filter(
    #         date__gte=datetime.date.today(),
    #         date__lte=datetime.date.today() + datetime.timedelta(days=7)
    #     ).values('master')
    #     print(master_calendar)
    #
    #     master = Master.objects.filter(id__in=master_calendar, status=True).values('service').distinct()
    #     print(master)
    #
    #     return Service.objects.filter(id__in=master)

    def get_queryset(self):
        queryset = super().get_queryset().filter(
            master__status=True,
            master__calendar__date__range=(datetime.date.today(), datetime.date.today() + datetime.timedelta(days=7))
        ).distinct()

        return queryset


class ServiceDetailView(DetailView):
    model = Service
    template_name = 'service/service.html'
    extra_context = {
        'title': 'Услуга',
        'subtitle': 'Lorem Ipsum'
    }
