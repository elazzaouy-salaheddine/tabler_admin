from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView,DetailView
from .models import AppointmentModel

class AppointmentListView(ListView):
    model = AppointmentModel
    template_name = 'appointments/appointment_list.html'
    context_object_name = 'appointments'
    paginate_by = 30  # TODO Number of appointments per page


    # Optionally, you can add queryset customization here if needed:
    # queryset = AppointmentModel.objects.filter(...)

    def get_queryset(self):
        # Customize the queryset here if needed
        return super().get_queryset()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add any additional context data here if needed
        return context


class AppointmentModelDetailView(DetailView):
    model = AppointmentModel
    template_name = 'appointments/appointmentmodel_detail.html'  # Specify your template
    context_object_name = 'appointment'  # Optional: Rename the context variable

class AppointmentCreateView(CreateView):
    model = AppointmentModel
    template_name = 'appointments/appointment_form.html'
    fields = ['Patient_Name', 'Department', 'Doctor', 'Date', 'Time', 'Patient_Email', 'Patient_Phone_Number',
              'Message', 'Appointment_Status']
    success_url = reverse_lazy('appointments:appointment_list')


class AppointmentUpdateView(UpdateView):
    model = AppointmentModel
    template_name = 'appointments/appointment_form.html'
    fields = ['Patient_Name', 'Department', 'Doctor', 'Date', 'Time', 'Patient_Email', 'Patient_Phone_Number',
              'Message', 'Appointment_Status']
    success_url = reverse_lazy('appointments:appointment_list')


class AppointmentDeleteView(DeleteView):
    model = AppointmentModel
    template_name = 'appointments/appointment_confirm_delete.html'
    success_url = reverse_lazy('appointments:appointment_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['appointment'] = self.object  # Pass the appointment object to the template
        return context
