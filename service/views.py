import datetime
from django.views.generic import DetailView, ListView
from django.shortcuts import redirect
from .models import Service
from master.models import Master
from booking.forms import BookingServiceForm
from booking.utils import calc_period
from booking.models import Booking


# Create your views here.
class ServiceListView(ListView):
    model = Service
    template_name = 'service/service_list.html'
    context_object_name = 'service_list'
    extra_context = {
        'title': 'Услуги',
        'subtitle': 'Список наших цен и услуг доступных в ближайшие 7 дней'
    }

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
        'subtitle': 'Детали услуги'
    }

    def get_form(self, master, date, free_time):
        form = BookingServiceForm(
            time_start_choices=[(time, time) for time in free_time],
            initial={
              'master': master.id,
              'date': date,
              'service': self.object.id,
              'user': self.request.user.id
            })

        return form

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        masters = Master.objects.filter(status=1, service=self.object)
        bookings = []
        for master in masters:
            forms = []
            for i in range(7):
                date = datetime.date.today() + datetime.timedelta(days=i)
                free_time = calc_period(master, self.object, date)
                if free_time:
                    forms.append(self.get_form(master, date, free_time))

            if forms:
                bookings.append({
                    'master': master,
                    'forms': forms
                })

        context['bookings'] = bookings
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        booking = Booking(
            master=Master.objects.get(id=request.POST.get('master')),
            user=self.request.user,
            service=self.object,
            date=request.POST.get('date'),
            time_start=request.POST.get('time_start')
        )
        booking.save()
        return redirect('/services', pk=kwargs['pk'])


