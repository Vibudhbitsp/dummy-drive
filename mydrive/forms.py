from django import forms
from django.db import models
from django.db.models import fields
from django.forms.forms import Form
from .models import * 
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields= [ 'username','password1','password2']

class DocumentForm(forms.Form):
    
    
    file = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
