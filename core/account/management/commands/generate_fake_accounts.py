from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from faker import Faker
from account.models import Profile, Department  # Import your models

class Command(BaseCommand):
    help = 'Generate fake data for Profile model'

    def handle(self, *args, **kwargs):
        fake = Faker()

        # Create fake profiles
        for _ in range(10):  # Generate 10 fake profiles (you can adjust the number)
            # Create a User instance
            user = User.objects.create_user(
                username=fake.user_name(),
                password='password123'  # Set a common password for all users
            )

            # Get a random Department
            department = Department.objects.order_by('?').first()

            # Create a Profile instance
            Profile.objects.create(
                user=user,
                bio=fake.paragraph(),
                location=fake.city(),
                phone_number=fake.phone_number(),
                department=department
            )

        self.stdout.write(self.style.SUCCESS('Fake profiles created successfully!'))
