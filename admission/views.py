# admission/views.py
from django.shortcuts import render, redirect
from .forms import AdmissionForm  # Ensure this import is correct



def index(request):
    return render(request, 'index.html')


# from django.shortcuts import render, redirect
from .forms import AdmissionForm

def admission_view(request):
    if request.method == 'POST':
        form = AdmissionForm(request.POST)
        if form.is_valid():
            # Process the form data (e.g., save to database)
            return redirect('success')  # Redirect to a success page or another view
    else:
        form = AdmissionForm()
    
    return render(request, 'admission.html', {'form': form})

def success_view(request):
    return render(request, 'success.html')



