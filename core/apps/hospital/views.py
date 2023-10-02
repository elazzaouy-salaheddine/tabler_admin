from django.shortcuts import render


# Create your views here.
def hospital_home(request):
    return render(request, template_name='hospital/index.html')
