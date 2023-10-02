from django.contrib.auth.decorators import login_required
from .forms import ProfileForm
from django.shortcuts import redirect
from django.shortcuts import render
from django.views.generic import DetailView, DeleteView
from django.urls import reverse_lazy
from .models import Profile
from django.shortcuts import render, redirect
from .forms import ProfileForm
from .models import Profile
from django.views import View
from django.utils.decorators import method_decorator





class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'profiles/profile_detail.html'
    context_object_name = 'profile'
    def get_object(self, queryset=None):
        # You can customize how the profile is retrieved, for example, based on the username.
        username = self.kwargs.get('username')  # Assuming you have a URL parameter 'username'.
        return Profile.objects.get(user__username=username)




class ProfileUpdateView(View):
    template_name = 'profiles/edit_profile.html'
    form_class = ProfileForm

    def get(self, request):
        form = self.form_class(instance=request.user.profile)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('appointments:appointment_list')  # Redirect to the user's profile page after editing.
        return render(request, self.template_name, {'form': form})



    
@method_decorator(login_required, name='dispatch')
class DeleteProfileView(DeleteView):
    model = Profile
    template_name = 'profiles/profile_confirm_delete.html'
    success_url = reverse_lazy('profiles:register')  # Redirect to your application's home page after deletion.
    context_object_name = 'user_profile'

    # Optionally, you can override the get_object method to fetch the user's profile.
    def get_object(self, queryset=None):
        return self.request.user.profile