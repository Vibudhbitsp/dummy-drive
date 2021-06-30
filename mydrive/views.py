from django import forms
from django.shortcuts import render,redirect
from django.http import HttpResponse, response,Http404
from .models import *
import os
from django.conf import settings
from .forms import *
from mydrive.function.functions import handle_uploaded_file
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def list(request):
    context = {'file': Document.objects.all()}
    return render(request,'mydrive/list.html',context)


@login_required
def upload(request):
    
    
    if request.method=="POST":
        form=DocumentForm(request.POST,request.FILES)
        files = request.FILES.getlist('file')
        if form.is_valid():
            for f in files:
                handle_uploaded_file(f)
                
                file = f
                title = f.name

                Document.objects.create(user=request.user,file = file,title=title)
            messages.success(request,f'CONGRATS , Your file is uploaded')
            return redirect('list')
    else:
        form=DocumentForm()
        return render(request,'mydrive/home.html',{'form':form})







def register(request):
    
    if request.method=="POST":
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'CONGRATS {username} !, Your profile is now created!')
            return redirect("list")
    else:
        user_form = UserRegisterForm()
        return render(request,'mydrive/register.html',{'user_form':user_form})

@login_required
def profile(request):
    return render(request, 'mydrive/profile.html')