from django.contrib import admin
from .models import Item, Category, Favorite, Friend, FriendRequests

# Register your models here.
class ItemAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        'author'
    )

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'category',
        'author'
    )

class FavoriteAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        'author'
    )


admin.site.register(Item, ItemAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Favorite, FavoriteAdmin)
admin.site.register(Friend)
admin.site.register(FriendRequests)