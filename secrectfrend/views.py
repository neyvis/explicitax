from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

import random

from django.utils import timezone
from .models import SecrectFriend

def friends_list(request):
    friends = User.objects.all()
    print(friends)
    return render(request, 'secrectfrend/friend_list.html', {'friends': friends})


from django.views.generic import ListView

class UserListView(ListView):
    model = User

def friend_detail(request, pk):
    friend = get_object_or_404(SecrectFriend, pk=pk)
    return render(request, 'secrectfrend/friend_detail.html', {'friend': friend})

@login_required(login_url="/accounts/login/")
def get_secrect_friend(request):
    my_id = request.user.id
    current_user, created = SecrectFriend.objects.get_or_create(user_id=my_id)
    if not current_user.secret_friend:
        availables = User.objects.exclude(
            secret_friend__id__isnull=False).exclude(id=my_id).values_list('pk', flat=True)
        if availables.exists():
            current_user.secret_friend_id = random.choice(availables)
            current_user.save()

    return render(request, 'secrectfrend/get_friend.html', {'friend': current_user.secret_friend})
