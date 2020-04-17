# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from .models import Task, TaskList
from django.contrib import admin

# Register your models here.


@admin.register(Task)
class Task(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_done')
    search_fields = ('name', )

@admin.register(TaskList)
class TaskList(admin.ModelAdmin):
    list_display = ('topic', 'created_by')
    search_fields = ('topic', )

