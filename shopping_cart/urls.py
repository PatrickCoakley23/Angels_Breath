from django.urls import path
from . import views

urlpatterns = [
    path('', views.shopping_cart, name='shopping_cart'),
    path('add/<sub_id>/<club_id>/', views.add_to_cart, name='add_to_cart'),
    path('update_cart/<club_id>', views.update_cart, name='update_cart'),
    #path('delete_sub/<sub_id>', views.delete_sub, name='delete_sub'),
    
]
