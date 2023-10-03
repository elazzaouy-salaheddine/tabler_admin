from django.urls import path
from . import views

urlpatterns = [
    path("", views.dashboard_home, name="dashboard_home"),
    path('profile/update/', views.UpdateUserProfileView.as_view(), name='update_profile'),
    path('dashboard_settings/', views.dashboard_settings, name='dashboard_settings'),
]
