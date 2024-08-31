
from django.urls import path
from . import views

urlpatterns = [

    path('', views.webapp, name= ""),
    path('register/', views.register, name= "register"),
    path('my_login', views.my_login, name= "my_login"),
    path('user_logout/', views.user_logout, name= "user_logout"),

    #CRUD
    path('dashboard/', views.dashboard, name= "dashboard"),
    path('create-record/', views.create_record, name= "create-record"),
    path('update_record/<int:pk>', views.update_record, name= "update_record"),
    path('view_record/<int:pk>', views.view_record, name= "view_record"),
    path('delete_record/<int:pk>', views.delete_record, name= "delete_record"),

]