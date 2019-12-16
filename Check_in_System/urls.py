from django.urls import path

from . import views

urlpatterns = [
    path('', views.Index, name='index'),
    path('register/',views.register,name='register'),
    path('activity/',views.activity,name='activity'),
    path('activity/show/<name>/',views.activityShow,name="activityShow"),
    path('activity/edit/',views.activityEdit,name="activityEdit")
]