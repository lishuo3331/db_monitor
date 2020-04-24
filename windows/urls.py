from django.urls import path
from windows import views

app_name = "windows"

urlpatterns = [
    path('api/windows-stat-list', views.ApiLinuxStatList.as_view()),
    path('api/windows-stat', views.ApiLinuxStat.as_view()),
    path('api/windows-stat-his', views.ApiLinuxStatHis.as_view()),
    path('api/windows-disk', views.ApiLinuxDisk.as_view()),
    path('api/windows-disk-his', views.ApiLinuxDiskHis.as_view()),
    path('api/windows-io-stat', views.ApiLinuxIoStat.as_view()),
    path('api/windows-io-stat-his', views.ApiLinuxIoStatHis.as_view()),
]

