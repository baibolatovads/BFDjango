from django.http import Http404
from rest_framework import generics, mixins
from rest_framework.permissions import IsAuthenticated

from api.models import Task
from api.serializers import TaskSerializer

from django.shortcuts import get_object_or_404

from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.response import Response
from rest_framework.decorators import action

class TaskListViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer