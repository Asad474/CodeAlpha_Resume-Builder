from .views import *
from django.urls import path 

urlpatterns = [
    path('', home, name = 'home'),
    path('login/', loginuser, name = 'loginuser'),
    path('logout/', logoutuser, name = 'logout'),
    path('register/', register, name = 'register'),
    path('resumeform/', resumeform, name='resume-form'),
    path('updateresume/', updateresume, name = 'updateresume'),
    path('resume/', resume, name = 'resume')
]