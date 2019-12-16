from django.urls import path

from . import views

urlpatterns = [
    path('', views.Index, name='index'),
    path('register/',views.register,name='register'),
<<<<<<< HEAD
    path('Changeinfo/',views.Changeinfo,name='Changeinfo'),
    
=======
    path('activity/',views.activity,name='activity'),
    path('activity/show/<name>/',views.activityShow,name="activityShow"),
    path('activity/edit/',views.activityEdit,name="activityEdit")
>>>>>>> d90dcfd0b3af974df823de5ff128c6988c49a747
]