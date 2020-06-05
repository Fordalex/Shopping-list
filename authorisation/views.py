from django.shortcuts import render, redirect
from items.models import Item, Category, Friend
from django.contrib.auth.models import User

def profile(request):
    Current_user = request.user.username
    items = Item.objects.filter(author=Current_user)
    category = Category.objects.filter(author=Current_user)
    users = User.objects.all()

    # Find the current users firends
    try:
        friend = Friend.objects.get(current_user=request.user)
        friends = friend.users.all()
    except:
        friends = None

    # Find the categories in use 
    categories_in_use = []
    for item in items:
        if item.category not in categories_in_use:
            categories_in_use.append(item.category)

    # count total items

    totalItems = len(items)

    content = {
        'items': items,
        'totalItems': totalItems,
        'categories': categories_in_use,
        'users': users,
        'friends': friends,

    }
    return render(request, 'profile.html', content)

def home(request):
    return render(request, 'home.html')