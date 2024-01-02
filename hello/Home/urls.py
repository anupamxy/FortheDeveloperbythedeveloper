from django.contrib import admin
from django.urls import path, include

from . import views
urlpatterns = [
    path('admin/', admin.site.urls),  # Admin URLs
    path('', include('home.urls')),  # Include home app URLs
    

    # Your custom URLs for update_view and detail_view
   
]
