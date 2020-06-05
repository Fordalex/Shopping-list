from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from .models import Favorite, Category, Item, Friend
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

   
    Item.objects.create(name=item_name.capitalize(), author=request.user.username, category=category)

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
    Item.objects.all().delete()
    return redirect('profile')

def change_friends(request, operation, pk):
    print(operation)
    print(pk)
    new_friend = User.objects.get(pk=pk)
    if operation == 'add':
        Friend.make_friend(request.user, new_friend)
        Friend.make_friend(new_friend, request.user)
    elif operation == 'remove':
        Friend.remove_friend(request.user, new_friend)
        Friend.remove_friend(new_friend, request.user)
    return redirect('profile')