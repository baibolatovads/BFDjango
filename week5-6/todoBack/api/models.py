# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from auth_.models import MyUser
# Create your models here.


class NotDoneTasks(models.Manager):
    def get_queryset(self):
        return self.filter(is_done=False)


class DoneTasks(models.Manager):
    def get_queryset(self):
        return self.filter(is_done=True)


class Task(models.Model):
    name = models.CharField(max_length=255)
    is_done = models.BooleanField(default=False)

    objects = models.Manager()
    not_done_tasks = NotDoneTasks()
    done_tasks = DoneTasks()

    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'

    def __str__(self):
        return '{}: {}'.format(self.id, self.name)


class TaskList(models.Model):
    topic = models.CharField(max_length=255)
    task = models.ForeignKey(Task, on_delete=models.CASCADE, default=None, blank=True)
    created_by = models.ForeignKey(MyUser, on_delete=models.CASCADE, default=1)

    class Meta:
        verbose_name = 'Task List'
        verbose_name_plural = 'Task Lists'

    def __str__(self):
        return '{}: {}'.format(self.id, self.topic)
