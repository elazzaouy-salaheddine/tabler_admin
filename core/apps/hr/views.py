from django.shortcuts import render


# Create your views here.
def hr_home(request):
    return render(request, template_name='hr/index.html')
