from django.shortcuts import render, redirect
from items.models import Item

def profile(request):
    items = Item.objects.filter(author=request.user.username)
    content = {
        'items': items
    }
    return render(request, 'profile.html', content)

def home(request):
    return render(request, 'home.html')