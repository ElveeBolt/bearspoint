import datetime
from django.shortcuts import redirect
from django.views.generic import DetailView, ListView
from .models import Master
from service.models import Service
from booking.forms import BookingServiceForm
from booking.utils import calc_period
from booking.models import Booking


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

    def get_form(self, service, date, free_time):
        form = BookingServiceForm(
            time_start_choices=[(time, time) for time in free_time],
            initial={
              'master': self.object.id,
              'date': date,
              'service': service.id,
              'user': self.request.user.id
            })

        return form

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        services = Service.objects.filter(master=self.object)
        print(services)
        bookings = []
        for service in services:
            forms = []
            for i in range(7):
                date = datetime.date.today() + datetime.timedelta(days=i)
                free_time = calc_period(master=self.object, service=service, date=date)
                if free_time:
                    forms.append(self.get_form(service, date, free_time))

            if forms:
                bookings.append({
                    'service': service,
                    'forms': forms
                })

        context['bookings'] = bookings
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        booking = Booking(
            master=self.object,
            user=self.request.user,
            service=Service.objects.get(id=request.POST.get('service')),
            date=request.POST.get('date'),
            time_start=request.POST.get('time_start')
        )
        booking.save()
        return redirect('/masters', pk=kwargs['pk'])