# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Profile, MyUser

# Register your models here.


class InlineProfile(admin.StackedInline):
    model = Profile
    verbose_name = 'Profile'
    verbose_name_plural = 'Profiles'
    can_delete = False


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'description', )


@admin.register(MyUser)
class MyUserAdmin(UserAdmin):
    inlines = (InlineProfile, )




