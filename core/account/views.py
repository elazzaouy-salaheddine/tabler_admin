from django.contrib.auth.decorators import login_required
from .forms import ProfileForm
from django.contrib.auth import login, authenticate
from django.shortcuts import redirect
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Department, Profile
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.urls import reverse
from .forms import CustomUserCreationForm
from .models import Profile

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
        user_form = CustomUserCreationForm(request.POST)
        if user_form.is_valid():
            # Create a new user account
            user = user_form.save()

            # Generate a password reset token
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            token = default_token_generator.make_token(user)

            # Build the password reset URL
            domain = get_current_site(request).domain
            reset_url = reverse('password_reset_confirm', kwargs={'uidb64': uid, 'token': token})
            reset_url = f'http://{domain}{reset_url}'

            # Send a password setup email to the user
            subject = 'Set Your Password'
            message = render_to_string('registration/password_setup_email.txt', {
                'user': user,
                'reset_url': reset_url,
            })
            from_email = 'your_email@example.com'  # Replace with your email address
            recipient_list = [user.email]
            send_mail(subject, message, from_email, recipient_list, fail_silently=False)

            # Log in the user
            login(request, user)

            # Create a corresponding profile for the user
            profile = Profile(user=user)
            profile.save()

            return redirect('profile-list')  # Redirect to a success page or profile list
    else:
        user_form = CustomUserCreationForm()

    return render(request, 'profiles/register.html', {'user_form': user_form})


class DepartmentListView(ListView):
    model = Department
    template_name = 'profiles/department_list.html'
    context_object_name = 'departments'


class DepartmentDetailView(DetailView):
    model = Department
    template_name = 'profiles/department_detail.html'
    context_object_name = 'department'


class ProfileListView(ListView):
    model = Profile
    template_name = 'profiles/profile_list.html'
    context_object_name = 'profiles'


class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'profiles/profile_detail.html'
    context_object_name = 'profile'


class ProfileCreateView(CreateView):
    model = Profile
    template_name = 'profiles/profile_form.html'
    fields = ['user', 'bio', 'location', 'phone_number', 'profile_pic', 'department']
    success_url = reverse_lazy('profiles:profile-list')


class ProfileUpdateView(UpdateView):
    model = Profile
    template_name = 'profiles/profile_form.html'
    fields = ['user', 'bio', 'location', 'phone_number','profile_pic', 'department']
    context_object_name = 'profile'
    success_url = reverse_lazy('profiles:profile-list')


class ProfileDeleteView(DeleteView):
    model = Profile
    template_name = 'profiles/profile_confirm_delete.html'
    context_object_name = 'profile'
    success_url = reverse_lazy('profiles:profile-list')
