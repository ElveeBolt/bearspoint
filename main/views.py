from django.views.generic import TemplateView
from master.models import Master
from service.models import Service


# Create your views here.
class IndexView(TemplateView):
    template_name = 'main/index.html'
    extra_context = {
        'title': 'BearsPoint',
        'subtitle': 'Мужское пространство, где вы можете позаботится о своём образе'
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['master_list'] = Master.objects.all()
        context['service_list'] = Service.objects.all()
        return context
