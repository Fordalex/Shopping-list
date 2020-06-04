from django.shortcuts import render, redirect
from items.models import Item, Category

def profile(request):
    items = Item.objects.filter(author=request.user.username)
    category = Category.objects.filter(author=request.user.username)

    # Find the categories in use 
    categories_in_use = []
    for item in items:
        if item.category not in categories_in_use:
            categories_in_use.append(item.category)

    content = {
        'items': items,
        'categories': categories_in_use,
    }
    return render(request, 'profile.html', content)

def home(request):
    return render(request, 'home.html')