from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class AppointmentDepartment(models.Model):
    name = models.CharField(max_length=100, default='None')
    def __str__(self):
        return self.name
class AppointmentModel(models.Model):
    Appointment_ID = models.AutoField(primary_key=True)
    Patient_Name = models.CharField(max_length=30)
    Department = models.ForeignKey(AppointmentDepartment, on_delete=models.CASCADE)
    Doctor = models.ForeignKey(User, on_delete=models.CASCADE, default=4)
    Date = models.DateField()
    Time = models.TimeField()
    Patient_Email = models.EmailField()
    Patient_Phone_Number = models.CharField(max_length=20, blank=True, null=True)
    Message = models.TextField(blank=True)
    Appointment_Status = models.BooleanField(default=False)

    def __str__(self):
        return f"Appointment ID: {self.Appointment_ID}, Patient: {self.Patient_Name}"

    def get_full_name(self):
        return f"{self.Doctor.first_name} {self.Doctor.last_name}"

    class Meta:
        ordering = ['-Date', '-Time']
