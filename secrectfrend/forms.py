from django.utils.translation import gettext_lazy as _
from django import forms

from .models import SecrectFriend

class SecrectFriendForm(forms.ModelForm):

    class Meta:
        model = SecrectFriend