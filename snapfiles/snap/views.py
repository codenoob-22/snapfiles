from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, HttpResponseRedirect, Http404
from snap.randomstr import randomString
from django.conf import settings
import uuid
import os
# Create your views here.

def upload(request):
    if request.method =="POST":
        uploaded_file = request.FILES['document']
        token = randomString()
        new_dir = os.path.join(settings.MEDIA_DIR,token)
        os.mkdir(new_dir)
        fs = FileSystemStorage(location=new_dir)
        name = fs.save(uploaded_file.name, uploaded_file)
        file_url = fs.url(name)
        print(file_url)
        return render(request,'url_view.html', { 'file_url':file_url,})

    return render(request,'upload.html')