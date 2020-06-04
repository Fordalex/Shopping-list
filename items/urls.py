from django.urls import path, include
from . import views

urlpatterns = [
    path('add_item/', views.add_item, name="add_item"),
    path('add_category/', views.add_category, name="add_category"),
    path('delete/<id>', views.delete, name="delete"),
    path('delete_all/', views.delete_all, name="delete_all"),
 
]
