from django.core.management.base import BaseCommand
from apps.crm.models import DelaiDePaiement  # Replace 'your_app' with the actual name of your app

class Command(BaseCommand):
    help = 'Generates fake data for the Categorie model based on a list'

    fake_categories = ["DelaiDePaiement1", "DelaiDePaiement2", "DelaiDePaiement3", "DelaiDePaiement4", "DelaiDePaiement5"]

    def handle(self, *args, **kwargs):
        for nom in self.fake_categories:
            DelaiDePaiement.objects.get_or_create(nom=nom)

        self.stdout.write(self.style.SUCCESS('Successfully generated fake categories.'))
