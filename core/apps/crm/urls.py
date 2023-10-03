from django.urls import path
from .views import (crm_home, ProjectListView, ProjectCreateView, ProjectDetailView,
                    ProjectUpdateView, ProjectDeleteView, CreateTaskView)
app_name = 'crm'
urlpatterns = [
    path("", crm_home, name="crm_home"),
    path('projects/', ProjectListView.as_view(), name='project-list'),
    path('projects/create/', ProjectCreateView.as_view(), name='project-create'),
    path('project/<int:pk>/', ProjectDetailView.as_view(), name='project-detail'),
    path('project/<int:pk>/update/', ProjectUpdateView.as_view(), name='project-update'),
    path('project/<int:pk>/delete/', ProjectDeleteView.as_view(), name='project-delete'),
    path('create-task/<int:pk>/', CreateTaskView.as_view(), name='create-task'),
]
