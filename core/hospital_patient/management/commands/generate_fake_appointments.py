from django.core.management.base import BaseCommand
from hospital_patient.models import AppointmentModel, AppointmentDepartment
from django.contrib.auth.models import User
from faker import Faker
import random
from datetime import datetime, timedelta


class Command(BaseCommand):
    help = 'Generate fake data for AppointmentModel'

    def handle(self, *args, **kwargs):
        fake = Faker()
        departments = AppointmentDepartment.objects.all()
        doctors = User.objects.filter(is_staff=True)

        num_records = 20  # Change this to the desired number of records

        for _ in range(num_records):
            appointment = AppointmentModel(
                Patient_Name=fake.name(),
                Department=random.choice(departments),
                Doctor=random.choice(doctors),
                Date=fake.date_between(start_date='-30d', end_date='+30d'),
                Time=fake.time(),
                Patient_Email=fake.email(),
                Patient_Phone_Number=fake.phone_number(),
                Message=fake.text(),
                Appointment_Status=random.choice([True, False])
            )
            appointment.save()
            self.stdout.write(self.style.SUCCESS(f'Created Appointment: {appointment}'))
