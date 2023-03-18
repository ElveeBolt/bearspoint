from django.views.generic import TemplateView


# Create your views here.
class BookingView(TemplateView):
    template_name = 'booking/service_list.html'
    extra_context = {
        'title': 'Бронирование',
        'subtitle': 'Lorem Ipsum'
    }
