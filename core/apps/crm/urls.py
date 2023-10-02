from django.urls import path
from .views import crm_home

urlpatterns = [
    path("", crm_home, name=""),
]
