from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Project,Task
from django.urls import reverse_lazy
from .forms import ProjectForm, TaskForm

class ProjectListView(LoginRequiredMixin, ListView):
    model = Project
    template_name = 'crm/projects/project_list.html'  # Create this HTML template in your app's templates directory
    context_object_name = 'projects'  # Specify the context variable name to use in the template
    ordering = ['-created_at']  # Sort projects by creation date (newest first)


class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project
    template_name = 'crm/projects/project_form.html'  # Create this HTML template in your app's templates directory
    form_class = ProjectForm
    success_url = reverse_lazy('crm:project-list')  # Redirect to the project list view upon successful submission

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ProjectDetailView(LoginRequiredMixin, DetailView):
    model = Project
    template_name = 'crm/projects/project_detail.html'  # Replace with the path to your HTML template
    context_object_name = 'project'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        project = self.object  # Get the project object

        # Retrieve tasks associated with the project
        tasks = Task.objects.filter(project=project)

        context['tasks'] = tasks  # Add tasks to the context

        # Add an empty TaskForm to the context for task creation
        context['task_form'] = TaskForm()
        return context

class CreateTaskView(CreateView):
    model = Task
    form_class = TaskForm  # Use the TaskForm for task creation
    template_name = 'crm/projects/project_detail.html'  # Replace with the path to your project detail template

    def form_valid(self, form):
        project_id = self.kwargs['pk']  # Get the project ID from the URL
        project = get_object_or_404(Project, id=project_id)
        form.instance.project = project
        return super().form_valid(form)
    def get_success_url(self):
        # Redirect to the project detail page with the project's ID
        return reverse_lazy('crm:project-detail', kwargs={'pk': self.kwargs['pk']})

class ProjectUpdateView(LoginRequiredMixin, UpdateView):
    model = Project
    template_name = 'crm/projects/project_form.html'  # Replace with the path to your HTML template
    fields = ['title', 'description', 'start_date', 'end_date']  # Add more fields if needed
    def get_success_url(self):
        # Specify the absolute URL you want to redirect to after a successful update
        return reverse_lazy('crm:project-detail', kwargs={'pk': self.object.pk})

class ProjectDeleteView(LoginRequiredMixin, DeleteView):
    model = Project
    template_name = 'crm/projects/project_confirm_delete.html'  # Replace with the path to your HTML template
    success_url = 'crm:project-list'  # Replace with the URL to redirect to after deletion
# Create your views here.
def crm_home(request):
    return render(request, template_name='crm/index.html')
