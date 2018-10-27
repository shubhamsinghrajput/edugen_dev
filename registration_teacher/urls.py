"""edugen URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
from registration_teacher import views

urlpatterns = [
    path('teacher/', views.teacher, name='teacher'),
    path('teacher_update/', views.teacher_update, name='teacher_update'),
    path('confirm_email/', views.confirm_email, name='confirm_email'),
    path('teacher_verify_otp/', views.teacher_verify_otp, name='teacher_verify_otp'),
]
