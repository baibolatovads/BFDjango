# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import MyUser
from .serializers import MyUserSerializer
# Create your views here.


class MyUserViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = MyUserSerializer
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        return MyUser.objects.all()

    @action(methods=['GET'], detail=False)
    def my_profile(self, request):
        serializer = self.get_serializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)


class RegisterUserApiView(APIView):
    http_method_names = ['post']

    def post(self, request):
        serializer = MyUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
