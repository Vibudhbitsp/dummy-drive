from os import name
from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('',list,name='list'),
    path('myfiles',upload,name='upload'),
]