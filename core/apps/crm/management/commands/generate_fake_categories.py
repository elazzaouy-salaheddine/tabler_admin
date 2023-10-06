from django.core.management.base import BaseCommand
from apps.crm.models import Categorie  # Replace 'your_app' with the actual name of your app

class Command(BaseCommand):
    help = 'Generates fake data for the Categorie model based on a list'

    fake_categories = ["Category1", "Category2", "Category3", "Category4", "Category5"]

    def handle(self, *args, **kwargs):
        for nom in self.fake_categories:
            Categorie.objects.get_or_create(nom=nom)

        self.stdout.write(self.style.SUCCESS('Successfully generated fake categories.'))
