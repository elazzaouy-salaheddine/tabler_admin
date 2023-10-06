from django.core.management.base import BaseCommand
from faker import Faker
from apps.crm.models import Compte, Categorie, Pays, Devise, DelaiDePaiement  # Replace 'your_app' with the actual name of your app
from django.contrib.auth.models import User  # Django's built-in User model

class Command(BaseCommand):
    help = 'Generates fake data for the Compte model'

    def handle(self, *args, **kwargs):
        fake = Faker()

        for _ in range(10):  # Generate 10 fake accounts, you can adjust the number as needed
            compte = Compte(
                type=fake.random_element(elements=Compte.TYPE_CHOICES)[0],
                raison_sociale=fake.company(),
                reference=fake.uuid4(),  # Generate a unique reference
                #registre_de_commerce=fake.unique.random_element([None, fake.random_int(10000, 99999)]),
                #ice=fake.unique.random_element([None, fake.random_int(10000, 99999)]),
                #societe_mere=fake.unique.random_element([None, fake.company()]),
                categorie=fake.random_element([None] + list(Categorie.objects.all())),
                pays=fake.random_element([None] + list(Pays.objects.all())),
                responsable=fake.random_element([None] + list(User.objects.all())),
                site_web=fake.url(),
                secteur_activite=fake.random_element([None, fake.word(ext_word_list=None)]),
                taille_fixe=fake.random_element([None, fake.random_int(1, 1000)]),
                taille_portable=fake.random_element([None, fake.random_int(1, 1000)]),
                fax=fake.random_element([None, fake.random_int(10000, 99999)]), # phone number
                devise=fake.random_element([None] + list(Devise.objects.all())),
                grille_tarifaire=fake.random_element([None, fake.word(ext_word_list=None)]),
                remise=fake.random_int(0, 100),
                delai_de_paiement=fake.random_element([None] + list(DelaiDePaiement.objects.all())),
                remarques=fake.random_element([None, fake.text()]),
                encours_initial=fake.random_int(0, 10000),
                adresse_facturation=fake.address(),
                code_postal_facturation=fake.zipcode(),
                ville_facturation=fake.city(),
                pays_facturation=fake.country(),
                adresse_livraison=fake.random_element([None, fake.address()]),
                code_postal_livraison=fake.random_element([None, fake.zipcode()]),
                ville_livraison=fake.random_element([None, fake.city()]),
                pays_livraison=fake.random_element([None, fake.country()]),
                rib=fake.random_element([None, fake.unique.iban()]),
                qui_a_acces=fake.random_element([choice[0] for choice in Compte.VISIBILITY_CHOICES]),
            )
            compte.save()

        self.stdout.write(self.style.SUCCESS('Successfully generated fake accounts.'))