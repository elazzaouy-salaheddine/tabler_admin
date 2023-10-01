from django.urls import path
from .views import AppointmentListView, AppointmentCreateView, AppointmentUpdateView, AppointmentDeleteView,AppointmentModelDetailView


app_name = 'appointments'
urlpatterns = [
    path('appointments/', AppointmentListView.as_view(), name='appointment_list'),
    path('appointments/create/', AppointmentCreateView.as_view(), name='appointment_create'),
    path('appointment/<int:pk>/', AppointmentModelDetailView.as_view(), name='appointment_detail'),
    path('appointments/<int:pk>/update/', AppointmentUpdateView.as_view(), name='appointment_update'),
    path('appointments/<int:pk>/delete/', AppointmentDeleteView.as_view(), name='appointment_delete'),
]
