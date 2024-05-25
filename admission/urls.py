# admission/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.admission_view, name='index'),
    path('admission/', views.admission_view, name='admission'),
    path('success/', views.success_view, name='success'),
    # Add other URL patterns as needed
]
