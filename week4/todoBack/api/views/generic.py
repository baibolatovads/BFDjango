from rest_framework import generics, mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from api.models import Task
from api.serializers import TaskSerializer

from django.shortcuts import get_object_or_404

from rest_framework.decorators import api_view
from rest_framework.views import APIView

from django.http import HttpRequest, HttpResponse, JsonResponse, Http404

from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status

from django.views import View
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView

from rest_framework import mixins


class TaskListAPIView(mixins.ListModelMixin, generics.GenericAPIView):
    http_method_names = ['GET', 'PUT']
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (IsAuthenticated, )

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class TaskCreateUpdateAPIView(mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
