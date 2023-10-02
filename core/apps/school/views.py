from django.shortcuts import render


# Create your views here.
def school_home(request):
    return render(request, template_name='school/index.html')
