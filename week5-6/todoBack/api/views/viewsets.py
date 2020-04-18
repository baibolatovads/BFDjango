from django.http import Http404
from rest_framework import generics, mixins
from rest_framework.permissions import IsAuthenticated

from api.models import Task, TaskList
from api.serializers import *

from django.shortcuts import get_object_or_404

from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.response import Response
from rest_framework.decorators import action
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

    serializer_class = TaskModelSerializer

    def perform_create(self, serializer):
        serializer.save()
        if self.action == 'create':
            logger.debug('Task is created, ID: {}'.format(serializer.instance))
            logger.info('Task is created, ID: {}'.format(serializer.instance))
            logger.warning('Task is created, ID: {}'.format(serializer.instance))
            logger.error('Task is created, ID: {}'.format(serializer.instance))
            logger.critical('Task is created, ID: {}'.format(serializer.instance))
        if self.action == 'update':
            logger.debug('Task is updated, ID: {}'.format(serializer.instance))
            logger.info('Task is updated, ID: {}'.format(serializer.instance))
            logger.warning('Task is updated, ID: {}'.format(serializer.instance))
            logger.error('Task is updated, ID: {}'.format(serializer.instance))
            logger.critical('Task is updated, ID: {}'.format(serializer.instance))
        if self.action == 'destroy':
            logger.debug('Task is deleted, ID: {}'.format(serializer.instance))
            logger.info('Task is deleted, ID: {}'.format(serializer.instance))
            logger.warning('Task is deleted, ID: {}'.format(serializer.instance))
            logger.error('Task is deleted, ID: {}'.format(serializer.instance))
            logger.critical('Task is deleted, ID: {}'.format(serializer.instance))

class TaskListViewSet(mixins.CreateModelMixin,
                      mixins.ListModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin,
                      viewsets.GenericViewSet):
    queryset = TaskList.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return TaskListShortSerializer
        if self.action == 'retrieve':
            return TaskListFullSerializer
        return TaskListShortSerializer

    def perform_create(self, serializer):
        serializer.save()
        logger.debug('Task List is created: {}'.format(serializer.instance))
        logger.info('Task List is created: {}'.format(serializer.instance))
        logger.warning('Task List is created: {}'.format(serializer.instance))
        logger.error('Task List is created: {}'.format(serializer.instance))
        logger.critical('Task List is created: {}'.format(serializer.instance))



