from django.core.management.base import BaseCommand
from django.db.utils import IntegrityError
from faker import Faker
from apps.crm.models import Pays  # Replace 'your_app' with the actual name of your app


class Command(BaseCommand):
    help = 'Generates fake data for the Pays model'

    def handle(self, *args, **kwargs):
        fake = Faker()

        for _ in range(10):  # Generate 10 fake countries, you can adjust the number as needed
            nom = fake.unique.country()

            try:
                Pays.objects.create(nom=nom)
            except IntegrityError:
                # Handle the case when a duplicate country name is generated (due to unique constraint)
                pass

        self.stdout.write(self.style.SUCCESS('Successfully generated fake countries.'))
