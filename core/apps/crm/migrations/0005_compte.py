# Generated by Django 4.2.5 on 2023-10-04 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("crm", "0004_alter_project_options_alter_task_options_lead"),
    ]

    operations = [
        migrations.CreateModel(
            name="Compte",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "type",
                    models.CharField(
                        choices=[("Professionnel", "Professionnel")], max_length=20
                    ),
                ),
                ("raison_sociale", models.CharField(max_length=255)),
                ("reference", models.CharField(blank=True, max_length=50, null=True)),
                (
                    "registre_de_commerce",
                    models.CharField(blank=True, max_length=50, null=True),
                ),
                ("ice", models.CharField(blank=True, max_length=50, null=True)),
                (
                    "societe_mere",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("categorie", models.CharField(blank=True, max_length=255, null=True)),
                ("responsable_email", models.EmailField(max_length=254)),
                ("site_web", models.URLField(blank=True, null=True)),
                (
                    "secteur_activite",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("taille_fixe", models.CharField(blank=True, max_length=15, null=True)),
                (
                    "taille_portable",
                    models.CharField(blank=True, max_length=15, null=True),
                ),
                ("fax", models.CharField(blank=True, max_length=15, null=True)),
                ("devise", models.CharField(max_length=10)),
                (
                    "grille_tarifaire",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                (
                    "remise",
                    models.DecimalField(decimal_places=2, default=0, max_digits=5),
                ),
                ("delai_de_paiement", models.CharField(max_length=50)),
                ("remarques", models.TextField(blank=True, null=True)),
                (
                    "encours_initial",
                    models.DecimalField(decimal_places=2, default=0, max_digits=10),
                ),
                ("adresse_facturation", models.CharField(max_length=255)),
                ("code_postal_facturation", models.CharField(max_length=20)),
                ("ville_facturation", models.CharField(max_length=100)),
                ("pays_facturation", models.CharField(max_length=100)),
                (
                    "adresse_livraison",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                (
                    "code_postal_livraison",
                    models.CharField(blank=True, max_length=20, null=True),
                ),
                (
                    "ville_livraison",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                (
                    "pays_livraison",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                ("rib", models.CharField(blank=True, max_length=50, null=True)),
                (
                    "qui_a_acces",
                    models.CharField(
                        choices=[
                            ("tout_le_monde", "Tout le monde a accès"),
                            (
                                "uniquement_le_responsable",
                                "Uniquement le responsable a accès",
                            ),
                            (
                                "certains_utilisateurs",
                                "Certains utilisateurs ont accès",
                            ),
                            ("certains_groupes", "Certains groupes ont accès"),
                        ],
                        default="tout_le_monde",
                        max_length=50,
                    ),
                ),
            ],
        ),
    ]
