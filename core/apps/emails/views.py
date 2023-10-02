from django.shortcuts import render


# Create your views here.
def emails_home(request):
    return render(request, template_name='emails/index.html')
