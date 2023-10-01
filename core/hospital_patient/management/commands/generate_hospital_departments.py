from django.core.management.base import BaseCommand
from hospital_patient.models import AppointmentDepartment
from faker import Faker

class Command(BaseCommand):
    help = 'Generate fake hospital departments'

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help='Indicate the total number of departments to create.')

    def handle(self, *args, **kwargs):
        fake = Faker()
        total = kwargs['total']

        for _ in range(total):
            name = fake.unique.job()  # Generate unique department names
            department = AppointmentDepartment(name=name)
            department.save()
            self.stdout.write(self.style.SUCCESS(f'Created Hospital Department: {department.name}'))
