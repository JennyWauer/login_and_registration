from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.home),
    path('success', views.success),
    path('register', views.register),
    path('user_login', views.user_login),
]