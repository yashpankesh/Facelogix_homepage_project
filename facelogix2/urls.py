"""
URL configuration for facelogix1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path,include
from . import views

app_name = 'facelogix2'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.HomePage,name="index"),
    path('login/',views.login,name='login'),
    path('profile/',views.profile,name='profile'),
    path('register/',views.Register,name='register'),
    path('Registeration', views.Registration, name='registeration'),
    path('aboutus/',views.AboutUs,name='aboutus'),
    path('contact/', views.contact, name='contact'),
    path('attendance/', views.Attendance, name='attendance'),
    path('capture/',views.capture,name="capture"),
    path('run-capture/', views.run_capture, name='run_capture'),
    # path('run_face_detection/', views.run_face_detection, name='run_face_detection'),
    path('capture_and_recognize_faces/', views.capture_and_recognize_faces, name='capture_and_recognize_faces'),
]
