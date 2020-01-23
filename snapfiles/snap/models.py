from django.db import models
from django import forms
from django.contrib.auth.models import User
from django.conf import settings
from .randomstr import randomString
import os

# Create your models here.   

class FileStore(models.Model):
    user =  models.ForeignKey(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=11, default=randomString, primary_key=True, unique=True)
    filename = models.CharField(max_length=11)
    is_checked = models.BooleanField(default=False)
    is_del = models.BooleanField(default=False)

    @property
    def get_dir(self):
        return os.path.join(settings.MEDIA_DIR, token)

