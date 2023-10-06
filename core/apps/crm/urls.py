from django.urls import path
from .views import (crm_home, ProjectListView, ProjectCreateView, ProjectDetailView,
                    ProjectUpdateView, ProjectDeleteView,
                    CreateTaskView, DeleteTaskView, UpdateTaskView,
                    LeadListView, LeadDetailView,LeadUpdateView, LeadDeleteView,
                    CompteListView, CompteDetailView, CompteUpdateView
                    )
app_name = 'crm'
urlpatterns = [
    path("", crm_home, name="crm_home"),
    path('projects/', ProjectListView.as_view(), name='project-list'),
    path('projects/create/', ProjectCreateView.as_view(), name='project-create'),
    path('project/<int:pk>/', ProjectDetailView.as_view(), name='project-detail'),
    path('project/<int:pk>/update/', ProjectUpdateView.as_view(), name='project-update'),
    path('project/<int:pk>/delete/', ProjectDeleteView.as_view(), name='project-delete'),
    path('create-task/<int:pk>/', CreateTaskView.as_view(), name='create-task'),
    path('task/update/<int:pk>/', UpdateTaskView.as_view(), name='update-task'),
    path('task/delete/<int:pk>/', DeleteTaskView.as_view(), name='delete-task'),

    path('leads/', LeadListView.as_view(), name='lead-list'),
    path('leads/<int:pk>/', LeadDetailView.as_view(), name='lead-detail'),
    path('leads/<int:pk>/update/', LeadUpdateView.as_view(), name='lead-update'),
    path('leads/<int:pk>/delete/', LeadDeleteView.as_view(), name='lead-delete'),

    path('comptes/', CompteListView.as_view(), name='compte-list'),
    path('comptes/<int:pk>/', CompteDetailView.as_view(), name='compte-detail'),
    path('comptes/<int:pk>/update/', CompteUpdateView.as_view(), name='compte-update'),
]
