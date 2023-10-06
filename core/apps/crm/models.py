from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.utils import timezone
# Common Choices
VISIBILITY_CHOICES = [
    ('tout_le_monde', 'Tout le monde a accès'),
    ('uniquement_le_responsable', 'Uniquement le responsable a accès'),
    ('certains_utilisateurs', 'Certains utilisateurs ont accès'),
    ('certains_groupes', 'Certains groupes ont accès'),
]

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
    TYPE_CHOICES = [
        ('Professionnel', 'Professionnel'),
        ('Fournisseur', 'Fournisseur'),
        ('Partenaire', 'Partenaire'),
    ]
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)

    raison_sociale = models.CharField(max_length=255)
    reference = models.CharField(max_length=50, blank=True, null=True)
    registre_de_commerce = models.CharField(max_length=50, blank=True, null=True)
    ice = models.CharField(max_length=50, blank=True, null=True)
    societe_mere = models.CharField(max_length=255, blank=True, null=True)
    categorie = models.ForeignKey(Categorie, on_delete=models.SET_NULL, blank=True, null=True)
    pays = models.ForeignKey(Pays, on_delete=models.SET_NULL, blank=True, null=True)
    responsable = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    site_web = models.URLField(blank=True, null=True)
    secteur_activite = models.CharField(max_length=255, blank=True, null=True)
    taille_fixe = models.CharField(max_length=15, blank=True, null=True)
    taille_portable = models.CharField(max_length=15, blank=True, null=True)
    fax = models.CharField(max_length=15, blank=True, null=True)
    devise = models.ForeignKey(Devise, on_delete=models.SET_NULL, blank=True, null=True)
    grille_tarifaire = models.CharField(max_length=255, blank=True, null=True)
    remise = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    delai_de_paiement = models.ForeignKey(DelaiDePaiement, on_delete=models.SET_NULL, blank=True, null=True)
    remarques = models.TextField(blank=True, null=True)
    encours_initial = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    adresse_facturation = models.CharField(max_length=255)
    code_postal_facturation = models.CharField(max_length=20)
    ville_facturation = models.CharField(max_length=100)
    pays_facturation = models.CharField(max_length=100)
    adresse_livraison = models.CharField(max_length=255, blank=True, null=True)
    code_postal_livraison = models.CharField(max_length=20, blank=True, null=True)
    ville_livraison = models.CharField(max_length=100, blank=True, null=True)
    pays_livraison = models.CharField(max_length=100, blank=True, null=True)
    rib = models.CharField(max_length=50, blank=True, null=True)
    qui_a_acces = models.CharField(max_length=50, choices=VISIBILITY_CHOICES, default='tout_le_monde')

    def __str__(self):
        return self.raison_sociale

    def save(self, *args, **kwargs):
        created = not self.pk  # Check if the instance is being created (no primary key yet)

        super().save(*args, **kwargs)  # Call the original save method to save the Compte

        # If the instance is being created (not updated)
        if created:
            # Create a Project related to this Compte (client)
            project = Project(
                client=self,  # Link the project to the client
                # Set other project-related fields as needed
            )
            project.save()  # Save the Project object

class Project(models.Model):
    title = models.CharField(max_length=200, default="This is the default project name.")
    description = RichTextField(default="This is the default text.")
    start_date = models.DateField(default=timezone.now)
    end_date = models.DateField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=255)
    client = models.ForeignKey(Compte, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']


class Invoice(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    invoice_number = models.CharField(max_length=50, default="INV0001")  # Default with "INV" and a unique number
    invoice_date = models.DateField(default=timezone.now)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    compte = models.ForeignKey(Compte, on_delete=models.CASCADE, related_name='invoices')

    def save(self, *args, **kwargs):
        if not self.invoice_number:
            # Generate a unique invoice number with "INV"
            last_invoice = Invoice.objects.order_by('-invoice_number').first()
            if last_invoice:
                last_number = int(last_invoice.invoice_number[3:])  # Extract the numeric part
                new_number = last_number + 1
                self.invoice_number = f"INV{str(new_number).zfill(4)}"  # Pad with leading zeros
            else:
                self.invoice_number = "INV0001"  # Initial invoice number

        super().save(*args, **kwargs)

    def __str__(self):
        return f"Invoice #{self.invoice_number} for {self.project.title}"
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
    STATUS_CHOICES = [
        ('New', 'New'),
        ('Contacted', 'Contacted'),
        ('Converted', 'Converted'),
        ('Closed', 'Closed'),
    ]
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    company = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='New')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='leads_created')
    created_for = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,
                                    related_name='leads_created_for')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        if self.status == 'Converted':
            self.convert_to_compte()
        super().save(*args, **kwargs)

    def convert_to_compte(self):
        compte = Compte(
            type='Professionnel',
            raison_sociale=f"{self.first_name} {self.last_name}",
        )
        compte.save()
    def delete(self, *args, **kwargs):
        # Delete related Compte and its related models
        if self.status == 'Converted':
            try:
                compte = Compte.objects.get(raison_sociale=f"{self.first_name} {self.last_name}")
                compte.delete()
            except Compte.DoesNotExist:
                pass
        super().delete(*args, **kwargs)
