from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from account.models import Department, Profile
from faker import Faker
import random

class Command(BaseCommand):
    help = 'Generate fake data for Department and Profile models'

    def handle(self, *args, **kwargs):
        fake = Faker()

        # Create fake departments
        departments = ['Department A', 'Department B', 'Department C', 'Department D']
        for department_name in departments:
            Department.objects.create(name=department_name)

        # Create fake users and profiles
        for _ in range(10):  # Create 10 fake users
            # Generate fake user data
            username = fake.unique.user_name()
            first_name = fake.first_name()
            last_name = fake.last_name()
            email = fake.email()
            password = User.objects.make_random_password()

            # Create a User instance
            user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, password=password)

            # Generate fake profile data
            bio = fake.text(max_nb_chars=500)
            location = fake.city()
            phone_number = fake.phone_number()
            profile_pic = f"profile_pics/{random.randint(1, 5)}.jpg"  # Assuming you have image files in 'profile_pics' folder

            # Get a random department
            department = random.choice(Department.objects.all())

            # Create a Profile instance associated with the User
            Profile.objects.create(user=user, bio=bio, location=location, phone_number=phone_number, profile_pic=profile_pic, department=department)

        self.stdout.write(self.style.SUCCESS('Successfully generated fake data.'))
