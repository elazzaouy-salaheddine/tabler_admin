from django.shortcuts import render


# Create your views here.
def hotel_home(request):
    return render(request, template_name='hotel/index.html')
