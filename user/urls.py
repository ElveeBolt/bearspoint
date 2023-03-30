from django.urls import path
from .views import UserView, ManagerMasterListView, ManagerMasterUpdateView, ManagerMasterCreateView, \
    ManagerMasterDeleteView

urlpatterns = [
    path('', UserView.as_view(), name='user'),
    path('manager/masters', ManagerMasterListView.as_view(), name='manager_masters'),
    path('manager/masters/<int:pk>', ManagerMasterUpdateView.as_view(), name='manager_master'),
    path('manager/masters/add', ManagerMasterCreateView.as_view(), name='manager_masters_add'),
    path('manager/masters/delete/<int:pk>', ManagerMasterDeleteView.as_view(), name='manager_masters_delete')
]
