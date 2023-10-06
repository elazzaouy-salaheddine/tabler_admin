import random
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from faker import Faker
from apps.crm.models import Task, Project

fake = Faker()

class Command(BaseCommand):
    help = 'Generate fake tasks for a specific project'

    def add_arguments(self, parser):
        parser.add_argument('num_tasks', type=int, help='Number of fake tasks to generate')

    def handle(self, *args, **kwargs):
        num_tasks = kwargs['num_tasks']

        users = User.objects.all()  # Get all user objects
        num_users = len(users)
        projects = Project.objects.all()
        num_projects = len(projects)

        for _ in range(num_tasks):
            title = fake.text(max_nb_chars=50)
            description = fake.paragraph()
            due_date = fake.date_between(start_date="today", end_date="+1y")
            assigned_to = random.choice(users) if num_users > 0 else None  # Choose a random user if any users exist
            project = random.choice(projects) if num_projects > 0 else None  # Choose a random project if any projects exist
            completed = fake.boolean(chance_of_getting_true=50)  # Randomly set completion status
            created_by = random.choice(users) if num_users > 0 else None
            task = Task(
                project=project,  # Assign the task to the retrieved project
                title=title,
                description=description,
                due_date=due_date,
                assigned_to=assigned_to,
                completed=completed,
                created_by=created_by,
            )
            task.save()

        self.stdout.write(
            self.style.SUCCESS(f'Successfully generated {num_tasks} fake tasks for projects.'))
