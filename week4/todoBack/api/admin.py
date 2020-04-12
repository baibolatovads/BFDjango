# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from .models import Task
from django.contrib import admin

# Register your models here.


@admin.register(Task)
class Task(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_done', 'created_by')
    search_fields = ('name', )
