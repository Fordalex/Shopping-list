from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from .models import Favorite, Category, Item, Friend, FriendRequests
from django.contrib.auth.models import User


# Create your views here.
def items(request):
    favorite = Favorite.objects.filter(author=request.user.username)
    category = Category.objects.filter(author=request.user.username)

    content = {
        'favorite': favorite,
        'categories': category,
    }
    return render(request, 'items/add_items.html', content)

def add_item(request):
    item_name = request.POST.get('item')  
    category = request.POST.get('category')

    # count items of the same name already in the database
    quantity = request.POST.get('quantity')
    try:
        print('in basket')
        in_basket = Item.objects.get(name=item_name.capitalize(), author=request.user.username)
        quantity_in_basket = in_basket.quantity
        in_basket.delete()
    except: 
        print('none in basket')
        quantity_in_basket = 0
    total_quantity = int(quantity) + int(quantity_in_basket)

    # create object
    Item.objects.create(name=item_name.capitalize(), author=request.user.username, category=category, quantity=total_quantity)

    #check if favorite already exists
    if request.POST.get('favorite'):
        try:
            item_exists = Favorite.objects.get(name=item_name.capitalize())
        except: 
            item_exists = False
    
        if not item_exists: 
            Favorite.objects.create(name=item_name.capitalize(), author=request.user.username, category=category)

    return redirect('profile')

def add_category(request):
    category = request.POST.get('category')
    Category.objects.create(category=category, author=request.user.username)
    return redirect('items')

def remove_category(request, id):
    category = get_object_or_404(Category, pk=id)
    category.delete()
    return redirect('items')

def remove_favorite(request, id):
    fav = get_object_or_404(Favorite, pk=id)
    fav.delete()
    return redirect('items')

def delete(request, id):
    item = get_object_or_404(Item, pk=id)
    item.delete()
    return redirect('profile')

def delete_all(request):
    items = Item.objects.all()
    items.delete()
    return redirect('profile')

def friend_request(request, pk):
    # add data to friend request with the current user and the user requested
    requested_user = User.objects.get(pk=pk)
    FriendRequests.objects.create(from_user=request.user, to_user=requested_user)

    return redirect('profile')

def change_friends(request, operation, pk):

    new_friend = User.objects.get(pk=pk)

    # remove friend request 
    try:
        friend_request = FriendRequests.objects.get(from_user=pk)
        friend_request.delete()
    except:
        friend_request = None
    
    # add or remove user from friend list
    if operation == 'add':
        Friend.make_friend(request.user, new_friend)
        Friend.make_friend(new_friend, request.user)
    elif operation == 'remove':
        Friend.remove_friend(request.user, new_friend)
        Friend.remove_friend(new_friend, request.user)
    return redirect('profile')