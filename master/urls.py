from django.urls import path
from .views import MasterListView, MasterDetailView

urlpatterns = [
    path('', MasterListView.as_view(), name='masters'),
    path('<int:pk>', MasterDetailView.as_view(), name='master'),
]