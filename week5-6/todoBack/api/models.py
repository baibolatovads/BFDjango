# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from auth_.models import MyUser
from utils.validators import validate_file_size, validate_extension
# Create your models here.


class NotDoneTasks(models.Manager):
    def get_queryset(self):
        return self.filter(is_done=False)


class DoneTasks(models.Manager):
    def get_queryset(self):
        return self.filter(is_done=True)


class Publisher(models.Model):
    MALE = 1
    FEMALE = 2
    GENDER = (
        (MALE, 'male'),
        (FEMALE, 'female'),
    )
    name = models.CharField(max_length=300, unique=True)
    city = models.CharField(max_length=300)
    gender = models.PositiveSmallIntegerField(choices=GENDER, default=MALE)

    objects = models.Manager()

    class Meta:
        verbose_name = 'Publisher'
        verbose_name_plural = 'Publishers'

    def __str__(self):
        return self.name


class UserPublisher(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE,
                             related_name='subscribed_publishers')
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE,
                                  related_name='subscribers')


class TaskList(models.Model):
    topic = models.CharField(max_length=255)
    created_by = models.ForeignKey(MyUser, on_delete=models.CASCADE, default=1)
    schedule = models.ImageField(upload_to='taskList_photos', validators=[validate_file_size,
                                                                          validate_extension],
                                                                          null=True, blank=True)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, related_name='tasks',
                                  default=None, null=True, blank=True)

    class Meta:
        verbose_name = 'Task List'
        verbose_name_plural = 'Task Lists'

    def __str__(self):
        return '{}: {}'.format(self.id, self.topic)


class Task(models.Model):
    name = models.CharField(max_length=255)
    is_done = models.BooleanField(default=False)
    task_list = models.ForeignKey(TaskList, on_delete=models.CASCADE, default=None, null=True, blank=True, related_name='tasks')

    objects = models.Manager()
    not_done_tasks = NotDoneTasks()
    done_tasks = DoneTasks()

    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'

    def __str__(self):
        return '{}: {}'.format(self.id, self.name)








