from django.urls import path
from .views import hospital_home

urlpatterns = [
    path("", hospital_home, name="hospital_home"),
]
