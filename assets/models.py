# encoding:utf-8
from django.db import models

# Create your models here.

# linux监控列表
class LinuxList(models.Model):

    LINUX_VERSION = [
        ('Linux6','Linux6'),
        ('Linux7', 'Linux7'),
    ]

    ALARM_CHOICES = [
        (0,'启用'),
        (1,'禁用')
    ]

    STATUS = [
        (0, '在线'),
        (1, '备用'),
        (2, '下线'),
        (3, '待用'),
        (4, '维修'),
        (5, '重装')    ]
    tags = models.CharField("标签",max_length=32,unique=True)
    host = models.CharField("主机ip",max_length=32)
    hostname = models.CharField("主机名",max_length=256)
    linux_version = models.CharField("linux版本",max_length=32,choices=LINUX_VERSION)
    linux_kernel = models.CharField("内核版本",max_length=64,blank=True,null=True)
    user = models.CharField("主机用户名",max_length=32)
    password = models.CharField("主机用户密码",max_length=255)
    sshport = models.IntegerField("主机ssh端口号",default=22)
    serialno = models.CharField("序列号",max_length=100,blank=True,null=True)
    status = models.IntegerField("状态",choices=STATUS,blank=True,null=True)
    cabinet = models.CharField("机柜",max_length=100,blank=True,null=True)
    factory = models.CharField("服务器厂家",max_length=100,blank=True,null=True)
    purchase_date = models.CharField("采购日期",max_length=32,blank=True,null=True)
    beginprotection_date = models.CharField("保修开始日期",max_length=32,blank=True,null=True)
    overprotection_date = models.CharField("过保日期",max_length=32,blank=True,null=True)
    bussiness_system = models.CharField("业务系统",max_length=255,blank=True,null=True)
    system_level = models.IntegerField("系统等级 0:核心系统 1:重要系统 2:一般系统",default=0)
    res_description = models.CharField("资源描述",max_length=255,blank=True,null=True)
    main_software = models.CharField("主要部署软件",max_length=255,blank=True,null=True)
    alarm_connect = models.IntegerField("通断告警",default=1)
    alarm_cpu = models.IntegerField("CPU使用率告警",default=1)
    alarm_mem = models.IntegerField("内存使用率告警",default=1)
    alarm_swap = models.IntegerField("swap使用率告警",default=1)
    alarm_disk = models.IntegerField("磁盘使用率告警",default=1)
    alarm_alert_log = models.IntegerField("后台日志告警",default=1)
    alert_log = models.CharField("后台日志路径",max_length=256,blank=True,null=True)

    def __str__(self):
        return self.tags

    class Meta:
        db_table = 'linux_list'
        verbose_name = "Linux主机"
        verbose_name_plural = verbose_name


class WindowsList(models.Model):

    LINUX_VERSION = [
        ('Linux6','Linux6'),
        ('Linux7', 'Linux7'),
    ]

    ALARM_CHOICES = [
        (0,'启用'),
        (1,'禁用')
    ]

    STATUS = [
        (0, '在线'),
        (1, '备用'),
        (2, '下线'),
        (3, '待用'),
        (4, '维修'),
        (5, '重装')    ]

    tags = models.CharField("标签",max_length=32,unique=True)
    host = models.CharField("主机ip",max_length=32)
    hostname = models.CharField("主机名",max_length=256)
    linux_version = models.CharField("linux版本",max_length=32,choices=LINUX_VERSION)
    linux_kernel = models.CharField("内核版本",max_length=64,blank=True,null=True)
    user = models.CharField("主机用户名",max_length=32)
    password = models.CharField("主机用户密码",max_length=255)
    sshport = models.IntegerField("主机ssh端口号",default=22)
    serialno = models.CharField("序列号",max_length=100,blank=True,null=True)
    status = models.IntegerField("状态",choices=STATUS,blank=True,null=True)
    cabinet = models.CharField("机柜",max_length=100,blank=True,null=True)
    factory = models.CharField("服务器厂家",max_length=100,blank=True,null=True)
    purchase_date = models.CharField("采购日期",max_length=32,blank=True,null=True)
    beginprotection_date = models.CharField("保修开始日期",max_length=32,blank=True,null=True)
    overprotection_date = models.CharField("过保日期",max_length=32,blank=True,null=True)
    bussiness_system = models.CharField("业务系统",max_length=255,blank=True,null=True)
    system_level = models.IntegerField("系统等级 0:核心系统 1:重要系统 2:一般系统",default=0)
    res_description = models.CharField("资源描述",max_length=255,blank=True,null=True)
    main_software = models.CharField("主要部署软件",max_length=255,blank=True,null=True)
    alarm_connect = models.IntegerField("通断告警",default=1)
    alarm_cpu = models.IntegerField("CPU使用率告警",default=1)
    alarm_mem = models.IntegerField("内存使用率告警",default=1)
    alarm_swap = models.IntegerField("swap使用率告警",default=1)
    alarm_disk = models.IntegerField("磁盘使用率告警",default=1)
    alarm_alert_log = models.IntegerField("后台日志告警",default=1)
    alert_log = models.CharField("后台日志路径",max_length=256,blank=True,null=True)

    def __str__(self):
        return self.tags

    class Meta:
        db_table = 'windows_list'
        verbose_name = "Windows主机"
        verbose_name_plural = verbose_name


# Redis监控列表
class RedisList(models.Model):

    REDIS_VERSION = [
        ('Redis3','Redis3')
    ]

    ALARM_CHOICES = [
        (0,'启用'),
        (1,'禁用')
    ]

    ROLE_CHOICES = [
        ('master','master'),
        ('slave','slave')
    ]

    tags = models.CharField("标签",max_length=32,unique=True)
    host = models.CharField("主机ip",max_length=32)
    port = models.IntegerField("数据库端口号",default=6379)
    password = models.CharField("密码",max_length=255,blank=True,null=True)
    linux_tags = models.CharField("所在linux主机标签",max_length=32,blank=True,null=True)
    redis_version = models.CharField("Redis版本",max_length=32,choices=REDIS_VERSION,blank=True,null=True)
    role = models.CharField("角色",max_length=32,choices=ROLE_CHOICES,blank=True,null=True)
    appdir = models.CharField("应用目录",max_length=128,blank=True,null=True)
    profile = models.CharField("配置文件",max_length=256,blank=True,null=True)
    architecture = models.CharField("架构(高可用)", max_length=32, blank=True, null=True)
    bussiness_system = models.CharField("业务系统", max_length=255, blank=True, null=True)
    system_level = models.IntegerField("系统等级 0:核心系统 1:重要系统 2:一般系统", default=0)
    res_description = models.CharField("资源描述", max_length=255, blank=True, null=True)
    alarm_connect = models.IntegerField("通断告警",default=1)
    alarm_alert_log = models.IntegerField("后台日志告警",default=1)
    log = models.CharField("后台日志路径",max_length=256,blank=True,null=True)
    log_seek = models.IntegerField("后台日志文件偏移量",blank=True,null=True)

    def __str__(self):
        return self.tags

    class Meta:
        db_table = 'redis_list'
        verbose_name = "Redis"
        verbose_name_plural = verbose_name
