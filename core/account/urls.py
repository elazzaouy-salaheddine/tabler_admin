from django.urls import path
from django.contrib.auth.views import (
    LoginView, LogoutView,
    PasswordChangeView, PasswordChangeDoneView,
    PasswordResetView,PasswordResetDoneView, PasswordResetConfirmView,PasswordResetCompleteView,
)
from .forms import PasswordResetForm, SetPasswordForm, PasswordChangeForm
from . import views
app_name = 'profiles'

urlpatterns = [

    # TODO path('sign_up/', MySignUpView.as_view(), name='sign_up'),
    path('login/', LoginView.as_view(template_name='profiles/login.html'), name='login_account'),
    path('logout/', LogoutView.as_view(template_name='profiles/logout.html'), name='logout_account'),

    path('password-change/', PasswordChangeView.as_view(template_name='profiles/password_change_form.html',
                                                        form_class=PasswordChangeForm), name='password_change'),
    path('password-change/done/', PasswordChangeDoneView.as_view(template_name='profiles/password_change_done.html',), name='password_change_done'),

    path('password-reset/', PasswordResetView.as_view(template_name='profiles/password_reset_form.html', form_class=PasswordResetForm,
                                                      email_template_name='profiles/password_reset_email.html'), name='password_reset'),
    path('password-reset/done/', PasswordResetDoneView.as_view(template_name='profiles/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='profiles/password_reset_confirm.html',
                                                                     form_class=SetPasswordForm), name='password_reset_confirm'),
    path('reset/done/', PasswordResetCompleteView.as_view(template_name='profiles/password_reset_complete.html'), name='password_reset_complete'),


    # TODO Department URLs

    # TODO Profile URLs
    path('<str:username>/', views.ProfileDetailView.as_view(), name='profile-detail'),
    path('profiles/update/', views.ProfileUpdateView.as_view(), name='profile-update'),
    path('<str:username>/delete_profile/', views.DeleteProfileView.as_view(), name='profile-delete'),

]
