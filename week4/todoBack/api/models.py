# -*- coding: utf-8 -*-
from django.db import models
from auth_.models import MyUser
# Create your models here.


class TaskManager(models.Manager):
    def for_user(self, user):
        return self.filter(created_by=user)


class Task(models.Model):
    name = models.CharField(max_length=255)
    is_done = models.BooleanField(default=False)
    created_by = models.ForeignKey(MyUser, on_delete=models.CASCADE, default=1)

    objects = TaskManager()

    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'

    def __str__(self):
        return '{self.name}: {self.created_by}'


