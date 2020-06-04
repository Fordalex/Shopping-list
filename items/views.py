from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from .models import Favorite, Category, Item

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
    Item.objects.create(name=item_name, author=request.user.username, category=category)

    if request.POST.get('favorite'):
        Favorite.objects.create(name=item_name, author=request.user.username, category=category)

    return redirect('profile')

def add_category(request):
    category = request.POST.get('category')
    Category.objects.create(category=category)
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