"""
URL configuration for internship_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin

from django.urls import path
from tasks.views import Hello,Task_list,create_task,delete_task,task_detail,edit_task,logoutUser
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
urlpatterns = [
    path("admin/", admin.site.urls),
    path("hello/",Hello,name='Hello'),
    path("tasks/",Task_list,name='task_list'),
    path("tasks/create",create_task,name='create_tasks'),
    path("task/<int:task_id>/",task_detail,name='task_detail'),
    path('task/<int:task_id>/delete/',delete_task,name='delete_task'),
    path('task/<int:task_id>/edit/',edit_task,name='edit_task'),
    
    path('login/', auth_views.LoginView.as_view(template_name='tasks/login.html'), name='login'),
    # path('logout/', auth_views.LogoutView.as_view(), name='logout'), 
    path('logout/',logoutUser,name='logout')

]
