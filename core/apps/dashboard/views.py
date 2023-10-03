from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from .models import UserProfile

# Create your views here.
def dashboard_home(request):
    return render(request, template_name='dashboard/index.html')

def dashboard_settings(request):
    return render(request, template_name='dashboard/settings.html')

@method_decorator(login_required, name='dispatch')
class UpdateUserProfileView(UpdateView):
    model = UserProfile
    fields = ['bio']  # Specify the fields you want to allow users to update
    template_name = 'dashboard/profiles/update_profile.html'
    success_url = reverse_lazy('dashboard_home')  # Replace 'profile' with your profile view name

    def get_object(self, queryset=None):
        return self.request.user.userprofile

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['user_fields'] = user  # Pass the User model instance to the template
        return context