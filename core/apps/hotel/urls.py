from django.urls import path
from .views import hotel_home

urlpatterns = [
    path("", hotel_home, name="hotel_home"),
]
