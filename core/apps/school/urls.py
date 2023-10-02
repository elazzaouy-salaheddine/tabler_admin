from django.urls import path
from .views import school_home

urlpatterns = [
    path("", school_home, name="school_home"),
]
