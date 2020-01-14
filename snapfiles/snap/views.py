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
        token = str(uuid.uuid1())
        tokenid = token
        new_dir = os.path.join(settings.MEDIA_DIR,token)
        os.mkdir(new_dir)
        fs = FileSystemStorage(location=new_dir)
        name = fs.save(uploaded_file.name, uploaded_file)
        file_url = fs.url(name)
        print(file_url)
        return render(request,'url_view.html', { 'token_id':token,})

    return render(request,'upload.html')

def get_files(request):
    # check wheter for a partiular token-id, folder exits or not
    if request.method =="POST":
        token = request.get('tokenID')
        dir_ = os.path.join(settings.MEDIA_DIR,token)
        if(os.path.exists(dir_)):
            ggg  = []  
        return render(request,'getfiles.html',{'result':'token Invalid!',})

    
    return render(request,'getfiles.html',{'result':'enter your token',})

