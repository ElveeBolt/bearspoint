from django.views.generic import TemplateView


# Create your views here.
class UserView(TemplateView):
    template_name = 'user/index.html'
    extra_context = {
        'title': 'Пользователь',
        'subtitle': 'Lorem'
    }
