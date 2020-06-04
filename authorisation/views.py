from django.shortcuts import render, redirect
from items.models import Item, Category

def profile(request):
    items = Item.objects.filter(author=request.user.username)
    category = Category.objects.filter(author=request.user.username)
    content = {
        'items': items,
        'categories': category,
    }
    return render(request, 'profile.html', content)

def home(request):
    return render(request, 'home.html')