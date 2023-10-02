from django.shortcuts import render


# Create your views here.
def dashboard_home(request):
    return render(request, template_name='dashboard/index.html')
