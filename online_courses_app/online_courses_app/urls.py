"""online_courses_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from main_app import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register', views.RegisterFormView.as_view()),
    path('login', views.LoginFormView.as_view()),
    path('logout', views.LogoutView.as_view()),
    path('', views.index, name='index'),
    path('personal', views.personal, name='personal'),
    path('course', views.course, name='course'),
    path('lecture', views.lecture, name='lecture'),
    path('homework', views.homework, name='homework'),
]
