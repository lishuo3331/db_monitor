from django.shortcuts import render

import json
import logging
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.authtoken.models import Token
from django.shortcuts import render, HttpResponse
from django.contrib.auth.backends import ModelBackend
from system.models import Users, ProcessInfo
from django.db.models import Q
from .models import AlertLog,AlarmConf,AlarmInfo
from rest_framework import permissions
from rest_framework import generics
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import AlertLogSerializer, AlarmConfSerializer, AlarmInfoSerializer, ProcessInfoSerializer

logger = logging.getLogger('system')

class UserInfo(APIView):
    """
    获取用户信息
    """
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        token = (json.loads(request.body))['token']
        obj = Token.objects.get(key=token).user
        result = {
            'name': obj.username,
            'user_id': obj.id,
            'access': list(obj.get_all_permissions()) + ['admin'] if obj.is_superuser else list(
                obj.get_all_permissions()),
            'token': token,
            'avatar': 'https://file.iviewui.com/dist/a0e88e83800f138b94d2414621bd9704.png'
        }
        return HttpResponse(json.dumps(result))

class UserLogout(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        token = (json.loads(request.body))['token']
        obj = Token.objects.get(key=token)
        obj.delete()
        result = {
            "status": True
        }
        return HttpResponse(json.dumps(result))


class CustomBackend(ModelBackend):
    """
    用户名字/邮箱名字 登录
    :param request:
    :return:
    """

    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = Users.objects.get(Q(username=username) | Q(email=username))
            if user.check_password(password):
                return user
        except Exception as e:
            logger.error(e)
            return None

class Menu(APIView):

    def post(self, request):
        result = [
            # {
            #     "path": '/assets',
            #     "name": 'assets',
            #     "meta": {
            #         "icon": 'ios-cloud',
            #         "title": '实例列表'
            #     },
            #     "component": 'Main',
            #     "children": [
            #
            #         {
            #             'path': 'linux-list',
            #             'name': 'linux-list',
            #             'meta': {
            #                 'access': ['assets.view_linuxlist'],
            #                 'icon': 'ios-menu',
            #                 'title': 'Linux主机'
            #             },
            #             'component': 'assets/linux-list'
            #         },
            #         # {
            #         #     'path': 'windows-list',
            #         #     'name': 'windows-list',
            #         #     'meta': {
            #         #         'access': ['assets.view_oraclelist'],
            #         #         'icon': 'ios-menu',
            #         #         'title': 'Windows主机'
            #         #     },
            #         #     'component': 'assets/oracle-list'
            #         # },
            #         {
            #             'path': 'windows-list',
            #             'name': 'windows-list',
            #             'meta': {
            #                 'access': ['assets.view_linuxlist'],
            #                 'icon': 'ios-menu',
            #                 'title': 'Windows主机'
            #             },
            #             'component': 'assets/windows-list'
            #         }
            #         # {
            #         #     'path': 'redis-list',
            #         #     'name': 'redis-list',
            #         #     'meta': {
            #         #         'access': ['assets.view_redislist'],
            #         #         'icon': 'ios-menu',
            #         #         'title': 'Redis'
            #         #     },
            #         #     'component': 'assets/redis-list'
            #         # }
            #     ]
            # },
            {
                "path": '/monlist',
                "name": '实例列表',
                "meta": {
                    "icon": 'ios-apps',
                    "title": '实例列表'
                },
                "component": 'Main',
                "children": [
                    # {
                    #     'path': 'oracle',
                    #     'name': 'oracle',
                    #     'meta': {
                    #         'icon': 'ios-menu',
                    #         'title': 'Oracle列表',
                    #         'access': ['oracle.view_oraclestat'],
                    #     },
                    #     'component': 'oracle/stat-list'
                    # },
                    # {
                    #     'path': 'redis',
                    #     'name': 'redis',
                    #     'meta': {
                    #         'icon': 'ios-menu',
                    #         'title': 'Redis列表',
                    #         'access': ['rds.view_redisstat'],
                    #     },
                    #     'component': 'redis/stat-list'
                    # },
                    {
                        'path': 'linux',
                        'name': 'linux',
                        'meta': {
                            'icon': 'ios-menu',
                            'title': 'Linux列表',
                            'access': ['oracle.view_oraclestat'],
                        },
                        'component': 'linux/stat-list'
                    },
                    {
                        'path': 'windows',
                        'name': 'windows',
                        'meta': {
                            'icon': 'ios-menu',
                            'title': 'Windows列表',
                            'access': ['oracle.view_oraclestat'],
                        },
                        'component': 'windows/stat-list'
                    }
                ],

            },
            {
                "path": '/process',
                "name": 'process',
                "meta": {
                    "icon": 'ios-warning',
                    "title": '进程列表'
                },
                "component": 'Main',
                "children": [
                    {
                        'path': 'preocess-info',
                        'name': 'preocess-info',
                        'meta': {
                            'access': ['system.view_alarminfo'],
                            'icon': 'ios-menu',
                            'title': '进程列表'
                        },
                        'component': 'system/process-info'
                    },
                    # {
                    #     'path': 'alarm-conf',
                    #     'name': 'alarm-conf',
                    #     'meta': {
                    #         'access': ['system.view_alarmconf'],
                    #         'icon': 'ios-menu',
                    #         'title': '告警配置'
                    #     },
                    #     'component': 'system/alarm-conf'
                    # }
                ]
            },
            {
                "path": '/alarm',
                "name": 'alarm',
                "meta": {
                    "icon": 'ios-warning',
                    "title": '监控告警'
                },
                "component": 'Main',
                "children": [
                    {
                        'path': 'alarm-info',
                        'name': 'alarm-info',
                        'meta': {
                            'access': ['system.view_alarminfo'],
                            'icon': 'ios-menu',
                            'title': '告警记录'
                        },
                        'component': 'system/alarm-info'
                    },
                    # {
                    #     'path': 'alarm-conf',
                    #     'name': 'alarm-conf',
                    #     'meta': {
                    #         'access': ['system.view_alarmconf'],
                    #         'icon': 'ios-menu',
                    #         'title': '告警配置'
                    #     },
                    #     'component': 'system/alarm-conf'
                    # }
                ]
            },

            {
                "path": '/linux',
                "name": 'Linux',
                "meta": {
                    'hideInMenu': 'true',
                    "icon": 'ios-apps',
                    "title": 'Linux主机监控'
                },
                "component": 'Main',
                "children": [
                    {
                        'path': ':tags/view',
                        'name': 'linux-view',
                        'meta': {
                            'hideInMenu': 'true',
                            'title': 'Linux概览',
                            'access': ['linux.view_linuxstat'],
                        },
                        'component': 'linux/view'
                    },
                    {
                        'path': ':tags/io',
                        'name': 'linux-io',
                        'meta': {
                            'hideInMenu': 'true',
                            'title': '磁盘IO',
                            'access': ['linux.view_linuxstat'],
                        },
                        'component': 'linux/io'
                    },
                    {
                        'path': ':tags/memory',
                        'name': 'linux-memory',
                        'meta': {
                            'hideInMenu': 'true',
                            'title': '内存&虚拟内存',
                            'access': ['linux.view_linuxstat'],
                        },
                        'component': 'linux/memory'
                    }
                ]
            },
            # {
            #     "path": '/multilevel',
            #     "name": 'multilevel',
            #     "meta": {
            #         "icon": 'md-menu',
            #         "title": '多级菜单'
            #     },
            #     "component": 'Main',
            #     "children": [
            #         {
            #             "path": '/level_2_1',
            #             "name": 'level_2_1',
            #             "meta": {
            #                 "icon": 'md-funnel',
            #                 "title": '二级-1'
            #             },
            #             "component": 'multilevel/level-2-1'
            #         },
            #
            #     ]
            # },
        ]
        return HttpResponse(json.dumps(result))

class ApiAlertLog(generics.ListAPIView):
    queryset = AlertLog.objects.all().order_by('-log_time')
    serializer_class = AlertLogSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filter_fields = ['tags','log_level']
    search_fields = ['log_content']
    permission_classes = (permissions.DjangoModelPermissions,)



class ApiAlarmConf(generics.ListCreateAPIView):
    queryset = AlarmConf.objects.get_queryset().order_by('-type')
    serializer_class = AlarmConfSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_fields = ('type','name',)
    search_fields = ('type','name',)
    permission_classes = (permissions.DjangoModelPermissions,)

class ApiAlarmConfDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = AlarmConf.objects.get_queryset().order_by('id')
    serializer_class = AlarmConfSerializer
    permission_classes = (permissions.DjangoModelPermissions,)

class ApiAlarmInfo(generics.ListCreateAPIView):
    def get_queryset(self):
        tags = self.request.query_params.get('tags', None)
        if tags:
            return AlarmInfo.objects.filter(tags=tags).order_by('id')
        else:
            print('index return alarm info ')
            return AlarmInfo.objects.all().order_by('-alarm_time')
    serializer_class = AlarmInfoSerializer
    print(serializer_class)
    permission_classes = (permissions.DjangoModelPermissions,)

class ApiProcessInfo(generics.ListCreateAPIView):
    def get_queryset(self):
        tags = self.request.query_params.get('tags', None)
        if tags:
            return ProcessInfo.objects.filter(tags=tags).order_by('id')
        else:
            print('index return alarm info ')
            # return ProcessInfo.objects.all().order_by('-alarm_time')
            return ProcessInfo.objects.all()
    serializer_class = ProcessInfoSerializer
    print(serializer_class)
    permission_classes = (permissions.DjangoModelPermissions,)


class ApiAlarmInfoHis(generics.ListCreateAPIView):
    queryset = AlarmInfo.objects.get_queryset().order_by('-id')
    serializer_class = AlarmInfoSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_fields = ('tags',)
    search_fields = ('tags','alarm_content',)
    permission_classes = (permissions.DjangoModelPermissions,)
