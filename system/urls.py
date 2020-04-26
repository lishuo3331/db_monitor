from django.urls import path
from system.views import UserInfo,UserLogout,Menu
from system import views

app_name = "system"

urlpatterns = [
    path('api/user_info', UserInfo.as_view()),
    path('api/logout', UserLogout.as_view()),
    path('menu', Menu.as_view()),
    path('api/alert-log', views.ApiAlertLog.as_view()),
    path('api/alarm-conf', views.ApiAlarmConf.as_view()),
    path('api/alarm-conf/<int:pk>', views.ApiAlarmConfDetail.as_view()),
    #首页获取告警信息
    path('api/alarm-info', views.ApiAlarmInfo.as_view()),
]
