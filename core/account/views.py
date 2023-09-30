from django.contrib.auth.decorators import login_required
from .models import Profile, Department
from .forms import ProfileForm
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
@login_required
def profile(request):
    profile = request.user.profile
    return render(request, 'profiles/profile.html', {'profile': profile})


@login_required
def edit_profile(request):
    profile = request.user.profile
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profiles:profile')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'profiles/edit_profile.html', {'form': form})


def register_user(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('profile')  # Replace 'profile' with the URL name for the user's profile page
    else:
        form = UserRegistrationForm()
    return render(request, 'profiles/register.html', {'form': form})




class UserProfileList(ListView):
    model = Profile
    template_name = 'profiles/user_profile_list.html'
    context_object_name = 'user_profiles'

class UserProfileCreate(CreateView):
    model = Profile
    template_name = 'profiles/user_profile_form.html'
    fields = ['user','bio','location','phone_number','email', 'department']
    success_url = reverse_lazy('profiles:user_profile_list')

class UserProfileUpdate(UpdateView):
    model = Profile
    template_name = 'profiles/user_profile_form.html'
    fields = ['user','bio','location','phone_number','email', 'department']
    success_url = reverse_lazy('profiles:user_profile_list')

class UserProfileDelete(DeleteView):
    # TODO DELETE PROFILE AND USER IN THE SAME TIME
    model = Profile
    template_name = 'profiles/user_profile_confirm_delete.html'
    success_url = reverse_lazy('profiles:user_profile_list')





