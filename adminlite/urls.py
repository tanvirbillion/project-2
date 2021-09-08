
from django.urls import path
from django.contrib.auth import  views as auth_views
from .views import *


urlpatterns = [
    path('', index, name="dashboard"),
    path('main/', main, name="main"),

]