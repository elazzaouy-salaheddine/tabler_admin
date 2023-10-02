from django.urls import path
from .views import emails_home

urlpatterns = [
    path("", emails_home, name="emails_home"),
]
