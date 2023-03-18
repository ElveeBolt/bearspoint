from django.views.generic import TemplateView


# Create your views here.
class IndexView(TemplateView):
    template_name = 'main/index.html'
    extra_context = {
        'title': 'BearsPoint',
        'subtitle': 'Мужское пространство, где вы можете позаботится о своём образе'
    }
