from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('upload/', views.upload, name='upload'),
    path('get_files/',views.get_files,name = 'get_files')
]