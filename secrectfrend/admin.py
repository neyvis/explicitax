from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import SecrectFriend


# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
class SecrectFriendInline(admin.StackedInline):
    model = SecrectFriend
    can_delete = False
    verbose_name_plural = "SecrectFriends"
    fk_name = "secret_friend"


# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = [SecrectFriendInline]


# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)