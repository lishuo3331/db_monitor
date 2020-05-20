from django.urls import path
from assets import views

app_name = "assets"

urlpatterns = [
    path('api/linux', views.ApiLinuxList.as_view()),
    path('api/linux/<int:pk>', views.ApiLinuxDetail.as_view()),
    path('api/windows', views.ApiWindowsList.as_view()),
    path('api/windows/<int:pk>', views.ApiWindowsDetail.as_view()),

]

