from django.urls import path
from .views import UserView, ManagerMasterListView, ManagerMasterUpdateView

urlpatterns = [
    path('', UserView.as_view(), name='user'),
    path('manager/masters', ManagerMasterListView.as_view(), name='manager_masters'),
    path('manager/masters/<int:pk>', ManagerMasterUpdateView.as_view(), name='manager_master'),
]