from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import Project
from django.urls import reverse_lazy

class ProjectListView(ListView):
    model = Project
    template_name = 'crm/projects/project_list.html'  # Create this HTML template in your app's templates directory
    context_object_name = 'projects'  # Specify the context variable name to use in the template
    ordering = ['-created_at']  # Sort projects by creation date (newest first)

class ProjectCreateView(CreateView):
    model = Project
    template_name = 'crm/projects/project_form.html'  # Create this HTML template in your app's templates directory
    fields = ['title', 'description', 'start_date', 'end_date']
    success_url = reverse_lazy('project-list')  # Redirect to the project list view upon successful submission


# Create your views here.
def crm_home(request):
    return render(request, template_name='crm/index.html')
