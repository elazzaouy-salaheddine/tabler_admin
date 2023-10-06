# yourapp/management/commands/generate_invoices.py

from django.core.management.base import BaseCommand
from django.utils import timezone
from faker import Faker
from apps.crm.models import Invoice, Project, Compte

class Command(BaseCommand):
    help = 'Generate fake invoices'

    def add_arguments(self, parser):
        parser.add_argument('--count', type=int, default=10, help='Number of invoices to generate')

    def handle(self, *args, **options):
        fake = Faker()

        # Get existing projects and comptes
        projects = Project.objects.all()
        comptes = Compte.objects.all()

        count = options['count']

        # Generate fake invoices
        for _ in range(count):
            project = fake.random_element(projects)
            compte = fake.random_element(comptes)
            invoice = Invoice(
                project=project,
                invoice_date=fake.date_this_decade(),
                total_amount=fake.random_number(digits=5) / 100,  # Adjust as needed
                compte=compte,
            )
            invoice.save()

        self.stdout.write(self.style.SUCCESS(f'Successfully generated {count} fake invoices.'))
