from django.urls import path
from . import views

urlpatterns = [
    path('', views.whiskey_clubs, name='clubs'),
    path('<club_id>', views.club_selected, name='club_selected'),
    path('choose/<int:club_id>/', views.choose_subscription,
         name='choose_subscription'),
]
