from django.urls import path
from . import views


urlpatterns = [
    #path('', views.post_list, name='PostListView'),
    path("", views.PostListView.as_view(), name="post-list"),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('postrandom/', views.random_post, name='random_post'),
]
