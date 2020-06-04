from django.shortcuts import render, redirect, get_object_or_404
from .models import Item, Category

# Create your views here.
def add_item(request):
    item_name = request.POST.get('item')  
    category = request.POST.get('category')
    Item.objects.create(name=item_name, author=request.user.username, category=category)
    return redirect('profile')

def add_category(request):
    category = request.POST.get('category')
    Category.objects.create(category=category)
    return redirect('profile')

def delete(request, id):
    item = get_object_or_404(Item, pk=id)
    item.delete()
    return redirect('profile')

def delete_all(request):
    Item.objects.all().delete()
    return redirect('profile')