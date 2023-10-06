from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from faker import Faker
from apps.crm.models import Lead  # Replace 'yourapp' with the name of your Django app

fake = Faker()

class Command(BaseCommand):
    help = 'Generate fake leads for testing purposes'

    def add_arguments(self, parser):
        parser.add_argument('num_leads', type=int, help='Number of fake leads to generate')

    def handle(self, *args, **kwargs):
        num_leads = kwargs['num_leads']

        users = User.objects.all()
        num_users = len(users)

        for _ in range(num_leads):
            first_name = fake.first_name()
            last_name = fake.last_name()
            email = fake.email()
            phone = fake.phone_number()
            company = fake.company()
            status = fake.random_element(elements=('New', 'Contacted', 'Converted', 'Closed'))
            created_by = fake.random_element(elements=users) if num_users > 0 else None
            created_for = fake.random_element(elements=users) if num_users > 0 else None

            lead = Lead(
                first_name=first_name,
                last_name=last_name,
                email=email,
                phone=phone,
                company=company,
                status=status,
                created_by=created_by,
                created_for=created_for,
            )
            lead.save()

        self.stdout.write(self.style.SUCCESS(f'Successfully generated {num_leads} fake leads'))
