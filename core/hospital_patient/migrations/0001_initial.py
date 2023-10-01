# Generated by Django 4.2.5 on 2023-09-30 13:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="AppointmentModel",
            fields=[
                ("Appointment_ID", models.AutoField(primary_key=True, serialize=False)),
                ("Patient_Name", models.CharField(blank=True, max_length=30)),
                ("Department", models.CharField(blank=True, max_length=20, null=True)),
                ("Date", models.DateField()),
                ("Time", models.TimeField()),
                ("Patient_Email", models.EmailField(max_length=254)),
                (
                    "Patient_Phone_Number",
                    models.CharField(blank=True, max_length=20, null=True),
                ),
                ("Message", models.TextField(blank=True)),
                ("Appointment_Status", models.BooleanField(default=False)),
                (
                    "Doctor",
                    models.ForeignKey(
                        default=4,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
