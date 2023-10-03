from django.urls import path
from .views import crm_home, ProjectListView, ProjectCreateView
app_name = 'crm'
urlpatterns = [
    path("", crm_home, name="crm_home"),
    path('projects/', ProjectListView.as_view(), name='project-list'),
    path('projects/create/', ProjectCreateView.as_view(), name='project-create'),
]
