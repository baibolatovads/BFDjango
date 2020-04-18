# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import Task, TaskList, Publisher

# Register your models here.


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_done')
    search_fields = ('name',)
    ordering = ('is_done',)


@admin.register(TaskList)
class TaskListAdmin(admin.ModelAdmin):
    list_display = ('id', 'topic', 'created_by')
    search_fields = ('topic', 'created_by', )


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
