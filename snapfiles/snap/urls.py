from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from . import views

urlpatterns = [
    path('upload/', views.upload, name='upload'),
    path('signup/',views.signup, name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('',views.home, name='home'),
    path('logout/', views.Logout, name='logout')
]
