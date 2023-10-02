from django.urls import path
from .views import hr_home

urlpatterns = [
    path("", hr_home, name=""),
]
