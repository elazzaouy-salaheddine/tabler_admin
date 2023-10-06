import random
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from faker import Faker
from apps.crm.models import Project  # Replace 'myapp' with the name of your Django app

fake = Faker()

class Command(BaseCommand):
    help = 'Generate fake projects'

    def add_arguments(self, parser):
        parser.add_argument('num_projects', type=int, help='Number of fake projects to generate')

    def handle(self, *args, **kwargs):
        num_projects = kwargs['num_projects']

        users = User.objects.all()  # Get all user objects
        num_users = len(users)

        for _ in range(num_projects):
            title = fake.text(max_nb_chars=50)
            description = fake.paragraph()
            start_date = fake.date_between(start_date="-1y", end_date="today")
            end_date = fake.date_between_dates(date_start=start_date, date_end="+1y")
            user = random.choice(users)  # Choose a random user from the list
            project = Project(
                title=title,
                description=description,  # Use generated paragraph as HTML content
                start_date=start_date,
                end_date=end_date,
                user=user,
            )
            project.save()

        self.stdout.write(self.style.SUCCESS(f'Successfully generated {num_projects} fake projects.'))
