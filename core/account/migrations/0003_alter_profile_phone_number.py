# Generated by Django 4.2.5 on 2023-09-29 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0002_customgroup"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="phone_number",
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
