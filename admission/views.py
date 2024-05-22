from django.shortcuts import render

# Create your views here.
# myapp/views.py

from django.shortcuts import render

def example_view(request):
    return render(request, '/example.html')


# admission/views.py

from django.http import HttpResponse

def admission_view(request):
    return HttpResponse("This is the admission page.")
