from django.shortcuts import render, redirect
from items.models import Item, Category, Friend
from django.contrib.auth.models import User

def profile(request):
    Current_user = request.user.username
    items = Item.objects.filter(author=Current_user)
    category = Category.objects.filter(author=Current_user)
    users = User.objects.all()
    friend = Friend.objects.get(current_user=request.user)
    friends = friend.users.all()


    # Find the categories in use 
    categories_in_use = []
    for item in items:
        if item.category not in categories_in_use:
            categories_in_use.append(item.category)

    content = {
        'items': items,
        'categories': categories_in_use,
        'users': users,
        'friends': friends,
    }
    return render(request, 'profile.html', content)

def home(request):
    return render(request, 'home.html')