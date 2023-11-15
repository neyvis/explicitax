from django.urls import path
from . import views


urlpatterns = [
    path("list/", views.FriendsListView.as_view(), name="friend-list"),
    path('friend/<int:pk>/', views.friend_detail, name='friend_detail'),
    path('my/friend/', views.get_secrect_friend, name='my_friend'),
]
