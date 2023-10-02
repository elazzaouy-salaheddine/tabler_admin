from django.urls import path
from .views import contact_home

urlpatterns = [
    path("", contact_home, name="contact"),
]
