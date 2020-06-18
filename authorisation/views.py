from django.shortcuts import render, redirect
from items.models import Item, Category, Friend, FriendRequests
from django.contrib.auth.models import User

def profile(request):
    Current_user = request.user.username
    items = Item.objects.filter(author=Current_user)
    category = Category.objects.filter(author=Current_user)
    users = User.objects.all()

    # Find the current users friends
    try:
        friend = Friend.objects.get(current_user=request.user)
        friends = friend.users.all()
    except:
        friends = None

    # get shopping parners request
    friendRequest = FriendRequests.objects.filter(to_user=request.user)

    # get sent requests
    sentRequests = FriendRequests.objects.filter(from_user=request.user)

    # all items
    allItems = items

    # collect partenrs items
    for friend in friends:
        friends_items = Item.objects.filter(author=friend.username)
        allItems = allItems | friends_items

    # Find the categories in use 
    categories_in_use = []
    for item in allItems:
        if item.category not in categories_in_use:
            categories_in_use.append(item.category)

    # data being passed into the profile page.
    content = {
        'items': allItems,
        'totalItems': len(allItems),
        'usersItems': len(items),
        'categories': categories_in_use,
        'friendRequests': friendRequest,
        'sentRequests': sentRequests,
        'friends': friends,
    }

    return render(request, 'profile.html', content)

def home(request):
    return render(request, 'home.html')