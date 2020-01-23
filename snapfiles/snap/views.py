

from django.http                    import HttpResponse, HttpResponseRedirect, Http404
from django.contrib.auth            import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms      import UserCreationForm
from django.core.files.storage      import FileSystemStorage
from django.shortcuts               import render, redirect
from django.conf                    import settings
from .models                         import FileStore
from snap.randomstr             import randomString
import os
import mimetypes

#user authentication and opening pages 
def home(request):
    return render(request, 'home.html')
#logout    
def Logout(request):
    logout(request)
    return redirect('home')    

def signup(request, error_message=None):
    if request.method =='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request,user)
            return redirect('home')
        else:
            error_message = "invalid format. Please try again"             
    form = UserCreationForm()
    return render(request,'registration/signup.html', {'form':form, 'error_message':error_message,})





@login_required
def upload(request):
    if request.method =="POST":
        uploaded_file = request.FILES['document']
        token = randomstr()
        new_dir = os.path.join(settings.MEDIA_DIR,token)
        os.mkdir(new_dir)
        fs = FileSystemStorage(location=new_dir)
        name = fs.save(uploaded_file.name, uploaded_file)
        file_url = fs.url(name)
        return render(request,'url_view.html', { 'token_id':token,})

    return render(request,'upload.html')

def sendFile(request):
    token = request.POST['token']
    

@login_required
def getFile(request, error_message=None):
    if request.method == 'POST':
        token = request.POST['token']
        if token_valid(token):
            return sendFile(request)
        else:
            error_message = "Token Invalid!"            

    return render(request, 'token_valid.html', error_message)
