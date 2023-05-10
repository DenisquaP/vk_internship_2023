from django.contrib import admin
from .models import (
    Users,
    Invites,
    Friends
)


@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    list_display = ('username',)
    list_filter = ('username',)


@admin.register(Friends)
class FriendsAdmin(admin.ModelAdmin):
    list_display = ('user', 'friend')
    list_filter = ('user', 'friend')


@admin.register(Invites)
class InvitesAdmin(admin.ModelAdmin):
    list_display = ('from_user', 'to_user',)
    list_filter = ('from_user', 'to_user',)
