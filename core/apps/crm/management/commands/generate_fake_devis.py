from django.core.management.base import BaseCommand
from django.db.utils import IntegrityError
from faker import Faker
from apps.crm.models import Devise  # Replace 'your_app' with the actual name of your app


class Command(BaseCommand):
    help = 'Generates fake data for the Devise model'

    def handle(self, *args, **kwargs):
        fake = Faker()

        for _ in range(10):  # Generate 10 fake currencies, you can adjust the number as needed
            code = fake.unique.random_element(["USD", "EUR", "GBP", "JPY", "CAD"])
            nom = fake.currency_name()

            try:
                Devise.objects.create(code=code, nom=nom)
            except IntegrityError:
                # Handle the case when a duplicate code is generated (due to unique constraint)
                pass

        self.stdout.write(self.style.SUCCESS('Successfully generated fake currencies.'))
