from django.shortcuts import render


# Create your views here.
def HospitalhomeView(request):
    return render(request, "hospital/home.html")
