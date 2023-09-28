from django.urls import path
from . import views


urlpatterns = [
    #path('', views.post_list, name='PostListView'),
    path("", views.PostListView.as_view(), name="post-list"),
]
