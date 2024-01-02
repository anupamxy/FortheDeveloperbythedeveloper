
from django.forms import ImageField
from django.shortcuts import (get_object_or_404,
                              render,redirect,
                              HttpResponseRedirect)

from django.shortcuts import render

from django.contrib.auth import authenticate, login, logout
from .models import Contact, MyModel
from django.utils import timezone  # For getting the current date and time
from .models import GeeksModel
from .forms import GeeksForm
from django.contrib import messages
from .imageform import MyModelForm
from django.contrib.auth.models import User

import json
import urllib.request
from django.shortcuts import render
from django.http import HttpResponseServerError
def welcome(request):
    return render(request,'welcome.html')

def index(request):
    if request.user.is_anonymous:
        return redirect('login')
    else:
        return render(request, 'index.html')



def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        desc2 = request.POST.get('desc2')
        contact = Contact(name=name, email=email, phone=phone, desc=desc,desc2=desc2, date=timezone.now())
        contact.save()
        messages.info(request, 'Message  Send bro!')


    return render(request, 'contact.html')

def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('welcome')
        else:
            # Handle invalid login credentials here
            # You might want to render the login page again with an error message
            return render(request, 'login.html', {'error_message': 'Invalid credentials'})

    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect('login')




def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        desc2 = request.POST.get('desc2')
        contact = Contact(name=name, email=email, phone=phone, desc=desc,desc2=desc2, date=timezone.now())
        contact.save()
        messages.info(request, 'Message  Send bro!')


    return render(request, 'contact.html')




def create_view(request):
    context = {}
    form = GeeksForm(request.POST or None)

    if form.is_valid():
        # Get the logged-in user
        user = User.objects.get(username=request.user.username)
        # Create content associated with the logged-in user using their username
        new_content = form.save(commit=False)
        new_content.user = user
        new_content.save()
        messages.success(request, 'Successfully created!')
        return redirect('list_view')

    context['form'] = form
    return render(request, "create_view.html", context)


def list_view(request):
    context = {}
    # Get the logged-in user
    user = User.objects.get(username=request.user.username)
    # Fetch content associated with the logged-in user using their username
    context["dataset"] = GeeksModel.objects.filter(user=user)
    return render(request, "list_view.html", context)

def update_view(request, title):
    obj = get_object_or_404(GeeksModel, title=title)
    form = GeeksForm(request.POST or None, instance=obj)
    
    if form.is_valid():
        form.save()
        messages.success(request, 'Successfully updated!')
        return redirect('list_view')
    context = {'form': form}
    return render(request, "create_view.html", context)
from django.shortcuts import get_object_or_404

def delete_item(request, title):
    # Retrieve the object based on the title and the logged-in user
    obj = get_object_or_404(GeeksModel, title=title, user=request.user)

    if request.method == "POST":
        # Delete the object
        obj.delete()
        messages.warning(request, 'Successfully deleted!')
        return redirect('list_view')

    return render(request, "delete_confirmation.html", {'object': obj})




def upload_image(request):
    if request.method == 'POST':
        form = MyModelForm(request.POST, request.FILES)
        if form.is_valid():
            new_image = form.save(commit=False)
            # Associate the image with the logged-in user's username
            user = User.objects.get(username=request.user.username)
            new_image.user = user
            new_image.save()
            # Handle success or redirect
            return redirect('display_images')
    else:
        form = MyModelForm()
    return render(request, 'upload_image.html', {'form': form})


def display_images(request):
    # Fetch images associated with the logged-in user's username
    images = MyModel.objects.filter(user=request.user)
    return render(request, 'display_image.html', {'images': images})
# views.py



# views.py



# views.py

# views.py



# views.py

# views.py

import json
import urllib.request
from django.shortcuts import render
from django.http import HttpResponse

def indian_news(request):
    url = 'https://indian-news1.p.rapidapi.com/indianNews'
    headers = {
        'X-RapidAPI-Key': '0f626657bamsh0ef7c86d9b9fba1p174806jsn4059fc13e714',
        'X-RapidAPI-Host': 'indian-news1.p.rapidapi.com'
    }
    params = {
        'size': '20',
        'cat': 'topNews'
    }

    try:
        req = urllib.request.Request(url, headers=headers)
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            raw_data = response.read()
            news_data = json.loads(raw_data).get('indianNews', {}).get('topNews', {}).get('articles', [])
            
            formatted_data = []
            for article in news_data:
                formatted_article = {
                    'title': article.get('title', ''),
                    'published_at': article.get('publishedAt', ''),  # You might want to format this date
                    'description': article.get('description', ''),
                    'author': article.get('author', ''),
                    'source': article.get('source', {}).get('name', ''),
                    'url': article.get('url', ''),
                    'urltoimage': article.get('urlToImage', '')
                }
                formatted_data.append(formatted_article)

            return render(request, 'news_template.html', {'news_data': formatted_data})
    except urllib.error.HTTPError as e:
        print(f"HTTPError: {e}")
    except urllib.error.URLError as e:
        print(f"URLError: {e}")
    
    return HttpResponse(status=500)  # Return an error response
