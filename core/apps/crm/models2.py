from django.db import models
from django.contrib.auth.models import User  # Django's built-in User model
from ckeditor.fields import RichTextField


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = RichTextField()
    start_date = models.DateField()
    end_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']


class Task(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    due_date = models.DateField()
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True,
                                   related_name='task_created_by')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']


class Lead(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    company = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, choices=[
        ('New', 'New'),
        ('Contacted', 'Contacted'),
        ('Converted', 'Converted'),
        ('Closed', 'Closed'),
    ], default='New')

    # Created by user
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='leads_created')

    # Created for user (optional)
    created_for = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,
                                    related_name='leads_created_for')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        # Check if the status is "Converted"
        if self.status == 'Converted':
            # Create a Compte object related to this Lead
            compte = Compte(
                type='Professionnel',  # Set the type as needed
                raison_sociale=f"{self.first_name} {self.last_name}",  # Use lead's name as company name
                # Populate other Compte fields as needed
            )
            compte.save()  # Save the Compte object

        super().save(*args, **kwargs)


class Categorie(models.Model):
    nom = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.nom


class DelaiDePaiement(models.Model):
    nom = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nom


class Devise(models.Model):
    code = models.CharField(max_length=10, unique=True)
    nom = models.CharField(max_length=50)

    def __str__(self):
        return self.nom


class Pays(models.Model):
    nom = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nom


class Compte(models.Model):
    # Type field
    TYPE_CHOICES = (
        ('Professionnel', 'Professionnel'),
        ('Fournisseur', 'Fournisseur'),
        ('Partenaire', 'Partenaire'),
        # Add other types if needed
    )
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)

    # General information
    raison_sociale = models.CharField(max_length=255)
    reference = models.CharField(max_length=50, blank=True, null=True)

    # Numérotation des comptes
    registre_de_commerce = models.CharField(max_length=50, blank=True, null=True)
    ice = models.CharField(max_length=50, blank=True, null=True)
    societe_mere = models.CharField(max_length=255, blank=True, null=True)
    categorie = models.ForeignKey(Categorie, on_delete=models.SET_NULL, blank=True, null=True)
    pays = models.ForeignKey(Pays, on_delete=models.SET_NULL, blank=True, null=True)
    # Responsable
    responsable = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    site_web = models.URLField(blank=True, null=True)
    secteur_activite = models.CharField(max_length=255, blank=True, null=True)

    # Taille
    taille_fixe = models.CharField(max_length=15, blank=True, null=True)
    taille_portable = models.CharField(max_length=15, blank=True, null=True)
    fax = models.CharField(max_length=15, blank=True, null=True)

    # Conditions de facturation
    devise = models.ForeignKey(Devise, on_delete=models.SET_NULL, blank=True, null=True)
    grille_tarifaire = models.CharField(max_length=255, blank=True, null=True)
    remise = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    delai_de_paiement = models.ForeignKey(DelaiDePaiement, on_delete=models.SET_NULL, blank=True, null=True)
    # Remarques
    remarques = models.TextField(blank=True, null=True)

    # Encours initial
    encours_initial = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    # Adresse de facturation
    adresse_facturation = models.CharField(max_length=255)
    code_postal_facturation = models.CharField(max_length=20)
    ville_facturation = models.CharField(max_length=100)
    pays_facturation = models.CharField(max_length=100)

    # Adresse de livraison (if different)
    adresse_livraison = models.CharField(max_length=255, blank=True, null=True)
    code_postal_livraison = models.CharField(max_length=20, blank=True, null=True)
    ville_livraison = models.CharField(max_length=100, blank=True, null=True)
    pays_livraison = models.CharField(max_length=100, blank=True, null=True)

    # Champs personnalisés
    rib = models.CharField(max_length=50, blank=True, null=True)

    # Visibilité
    VISIBILITY_CHOICES = (
        ('tout_le_monde', 'Tout le monde a accès'),
        ('uniquement_le_responsable', 'Uniquement le responsable a accès'),
        ('certains_utilisateurs', 'Certains utilisateurs ont accès'),
        ('certains_groupes', 'Certains groupes ont accès'),
    )
    qui_a_acces = models.CharField(max_length=50, choices=VISIBILITY_CHOICES, default='tout_le_monde')

    def __str__(self):
        return self.raison_sociale  # Display the company name as the model's string representation
