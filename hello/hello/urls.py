"""
URL configuration for hello project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include  # Import include here
from Home import views
from django.conf import settings
from django.conf.urls.static import static

# ... Your other URL patterns



urlpatterns = [
    path("admin/", admin.site.urls),  # Include admin URLs here
    path("welcome/", views.welcome, name='welcome'),
    path("", views.index, name='home'),
    path("contact", views.contact, name='contact'),
    path('login/', views.login_view, name='login'),
     path('logout/', views.logout_user, name='logout'),
     path('create_view/', views.create_view, name='create_view'),
     path('list_view/', views.list_view, name='list_view'),
    path('update_view/<str:title>/', views.update_view, name='update_view'),  # Use 'title' instead of 'id'
     path('delete/<str:title>/', views.delete_item, name='delete_item'),
     path('upload/', views.upload_image, name='upload_image.html'),
      path('display/', views.display_images, name='display_images'),
       path('newstemplate/', views.indian_news, name='news_template'),
     
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

