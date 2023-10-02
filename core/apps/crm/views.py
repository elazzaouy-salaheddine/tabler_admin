from django.shortcuts import render


# Create your views here.
def crm_home(request):
    return render(request, template_name='crm/index.html')
