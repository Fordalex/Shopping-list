from django.urls import path, include
from . import views

urlpatterns = [
    path('items/', views.items, name="items"),
    path('add_item/', views.add_item, name="add_item"),
    path('add_category/', views.add_category, name="add_category"),
    path('remove_category/<id>', views.remove_category, name="remove_category"),
    path('remove_favorite/<id>', views.remove_favorite, name="remove_favorite"),
    path('delete/<id>', views.delete, name="delete"),
    path('delete_all/', views.delete_all, name="delete_all"),
    path('connect/<operation>/<pk>', views.change_friends, name="change_friends"),
]
