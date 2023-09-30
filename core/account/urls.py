from django.urls import path
from .views import profile, edit_profile, register_user,UserProfileList, UserProfileCreate, UserProfileUpdate, UserProfileDelete
from django.contrib.auth.views import (
    LoginView, LogoutView,
    PasswordChangeView, PasswordChangeDoneView,
    PasswordResetView,PasswordResetDoneView, PasswordResetConfirmView,PasswordResetCompleteView,
)
from .forms import PasswordResetForm, SetPasswordForm, PasswordChangeForm
from . import views
app_name = 'profiles'

urlpatterns = [
    path('', profile, name='profile'),
    path('edit_profile/', edit_profile, name='edit_profile'),
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

    # TODO path('register/', register_user, name='register'),
    path('user_profiles/', UserProfileList.as_view(), name='user_profile_list'),
    path('user_profiles/create/', UserProfileCreate.as_view(), name='user_profile_create'),
    path('user_profiles/<int:pk>/update/', UserProfileUpdate.as_view(), name='user_profile_update'),
    path('user_profiles/<int:pk>/delete/', UserProfileDelete.as_view(), name='user_profile_delete'),

]
