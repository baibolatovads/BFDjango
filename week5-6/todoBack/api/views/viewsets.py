from django.http import Http404
from rest_framework import generics, mixins
from rest_framework.permissions import IsAuthenticated
from django.db.models import Avg, Max, Min, Sum, Count
from rest_framework.parsers import FormParser, MultiPartParser, JSONParser

from api.models import Task, TaskList
from api.serializers import *

from django.shortcuts import get_object_or_404

from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.parsers import FormParser, MultiPartParser, JSONParser
import logging

logger = logging.getLogger('api')

class TaskViewSet(mixins.CreateModelMixin,
                        mixins.ListModelMixin,
                       mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin,
                       viewsets.GenericViewSet):

    def get_queryset(self):
        is_done = self.request.query_params.get('is_done', None)
        if is_done is True:
            return Task.done_tasks.all()
        elif is_done is False:
            return Task.not_done_tasks.all()
        else:
            return Task.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return TaskShortSerializer
        if self.action == 'retrieve':
            return TaskFullSerializer
        return TaskShortSerializer

    def perform_create(self, serializer):
        serializer.save()
        logger.debug('Task is created, ID: {}'.format(serializer.instance))
        logger.info('Task is created, ID: {}'.format(serializer.instance))

    def perform_update(self, serializer):
        logger.debug('Task is updated, ID: {}'.format(serializer.instance))
        logger.info('Task is updated, ID: {}'.format(serializer.instance))
        logger.warning('Task is updated, ID: {}'.format(serializer.instance))

    def perform_destroy(self, instance):
        logger.warning('Task is deleted, ID: {}'.format(instance))

    @action(methods=['GET'], detail=False)
    def task_report(self, request):
        data = [
            TaskList.objects.values('id').annotate(Count('tasks'))
        ]
        return Response(data)


class TaskListViewSet(mixins.CreateModelMixin,
                      mixins.ListModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin,
                      viewsets.GenericViewSet):

    queryset = TaskList.objects.annotate(tasks_count=Count('tasks'))
    serializer_class = TaskListSerializer
    parser_classes = (FormParser, MultiPartParser, JSONParser)

    def get_queryset(self):
        if self.action == 'list':
            return TaskList.objects.prefetch_related('tasks')
        return TaskList.objects.all()

    def perform_create(self, serializer):
        serializer.save()
        logger.debug('Task List is created: {}'.format(serializer.instance))
        logger.info('Task List is created: {}'.format(serializer.instance))

    def perform_update(self, serializer):
        logger.debug('Task List is updated, ID: {}'.format(serializer.instance))
        logger.info('Task List is updated, ID: {}'.format(serializer.instance))
        logger.warning('Task List is updated, ID: {}'.format(serializer.instance))

    def perform_destroy(self, instance):
        logger.warning('Task List is deleted, ID: {}'.format(instance))

