from django.shortcuts import render


# Create your views here.
def task_home(request):
    return render(request, template_name='task/index.html')
