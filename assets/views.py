# encoding:utf-8

from .models import *
from rest_framework import permissions
from rest_framework import generics
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

from .serializers import *

# Ecs Api           drf 中文文档   http://drf.jiuyou.info/#/drf/requests


class ApiLinuxList(generics.ListCreateAPIView):
    queryset = LinuxList.objects.get_queryset().order_by('id')
    serializer_class = LinuxListSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_fields = ('tags', 'host','linux_version')
    search_fields = ('tags', 'host',)
    permission_classes = (permissions.DjangoModelPermissions,)  # 继承 django的权限

class ApiLinuxDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = LinuxList.objects.get_queryset().order_by('id')
    serializer_class = LinuxListSerializer
    permission_classes = (permissions.DjangoModelPermissions,)

class ApiWindowsList(generics.ListCreateAPIView):
    queryset = WindowsList.objects.get_queryset().order_by('id')
    serializer_class = LinuxListSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_fields = ('tags', 'host','linux_version')
    search_fields = ('tags', 'host',)
    permission_classes = (permissions.DjangoModelPermissions,)  # 继承 django的权限

class ApiWindowsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = WindowsList.objects.get_queryset().order_by('id')
    serializer_class = LinuxListSerializer
    permission_classes = (permissions.DjangoModelPermissions,)
