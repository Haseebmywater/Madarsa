
# project/urls.py


from django.contrib import admin
from django.urls import path, include
from admission import views  # Import views module from your project

urlpatterns = [
    path('', views.index, name='index'),  # Define the index URL pattern
    path('admin/', admin.site.urls),
    path('admission/', include('admission.urls')),
]


