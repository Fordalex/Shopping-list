from django.shortcuts import render
from .models import Item

# Create your views here.
def add_item(request):
    item_name = request.POST.get('item')  
    Item.objects.create(name=item_name, author=request.user.username)
    return redirect('profile')

def delete(request, id):
    item = get_object_or_404(Item, pk=id)
    item.delete()
    return redirect('profile')
