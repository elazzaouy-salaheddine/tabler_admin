from django.contrib import admin
from .models import AppointmentModel, AppointmentDepartment


class AppointmentModelAdmin(admin.ModelAdmin):
    list_display = ["Patient_Name", "Department", "Doctor", "Patient_Phone_Number"]
    list_filter = ["Department"]
    search_fields = ["Patient_Name"]


admin.site.register(AppointmentModel, AppointmentModelAdmin)
# Register your models here.
admin.site.register(AppointmentDepartment)