from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Project, Task, Lead, Compte, Invoice
from django.urls import reverse_lazy
from .forms import ProjectForm, TaskForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse
class ProjectListView(LoginRequiredMixin, ListView):
    model = Project
    template_name = 'crm/projects/project_list.html'  # Create this HTML template in your app's templates directory
    context_object_name = 'projects'  # Specify the context variable name to use in the template
    ordering = ['-created_at']  # Sort projects by creation date (newest first)
    paginate_by = 10


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
@method_decorator(login_required, name='dispatch')
class CreateTaskView(CreateView):
    model = Task
    form_class = TaskForm  # Use the TaskForm for task creation
    template_name = 'crm/projects/project_detail.html'  # Replace with the path to your project detail template

    def form_valid(self, form):
        project_id = self.kwargs['pk']  # Get the project ID from the URL
        project = get_object_or_404(Project, id=project_id)
        form.instance.project = project
        form.instance.created_by = self.request.user
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


class UpdateTaskView(UpdateView):
    model = Task
    form_class = TaskForm  # Use the TaskForm for updating tasks
    template_name = 'crm/projects/task_update.html'  # Replace with your template path

    def get_success_url(self):
        # Get the project associated with the updated task
        project = self.object.project
        return reverse_lazy('crm:project-detail', kwargs={'pk': project.id})

class DeleteTaskView(DeleteView):
    model = Task
    template_name = 'crm/projects/task_confirm_delete.html'  # Replace with your template path
    def get_success_url(self):
        # Get the project associated with the deleted task
        project = self.object.project
        return reverse_lazy('crm:project-detail', kwargs={'pk': project.id})


class LeadListView(ListView):
    model = Lead  # Specify the model to use (Lead)
    template_name = 'crm/leads/lead_list.html'  # Replace with the path to your HTML template
    context_object_name = 'leads'  # Customize the context variable name (default is 'object_list')
    #paginate_by = 10  # Number of leads per page (adjust as needed)

class LeadDetailView(DetailView):
    model = Lead
    template_name = 'crm/leads/lead_detail.html'  # Replace with your template name
    context_object_name = 'lead'
class LeadUpdateView(UpdateView):
    model = Lead
    template_name = 'crm/leads/lead_form.html'  # Create this template
    fields = ['first_name', 'last_name', 'email', 'phone', 'company', 'status']  # Update fields as needed

    def get_success_url(self):
        return reverse_lazy('crm:lead-detail', kwargs={'pk': self.object.pk})
class LeadDeleteView(DeleteView):
    model = Lead
    template_name = 'crm/leads/lead_confirm_delete.html'  # Create this template
    success_url = reverse_lazy('crm:lead-list')  # Define the URL to redirect after deletion

class CompteListView(ListView):
    model = Compte
    template_name = 'crm/compte/compte_list.html'  # Replace with your template name
    context_object_name = 'comptes'


class CompteDetailView(DetailView):
    model = Compte
    template_name = 'crm/compte/compte_detail.html'  # Replace with your template name
    context_object_name = 'compte'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        compte = self.get_object()  # Retrieve the Compte object

        # Get related invoices for the Compte
        invoices = Invoice.objects.filter(compte_id=compte.pk) # Assuming "invoice_set" is the related name in the Invoice model

        context['invoices'] = invoices
        return context

class CompteUpdateView(UpdateView):
    model = Compte
    template_name = 'crm/compte/compte_form.html'  # Replace with your template name
    fields = '__all__'
    def form_valid(self, form):
        compte = form.save()
        return redirect(reverse('crm:compte-detail', args=[compte.pk]))


