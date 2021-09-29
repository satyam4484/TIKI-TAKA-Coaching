
from django.urls import path 

from .views import (UserSignup ,UserLogin,ParentHome,PlayerHome)
urlpatterns = [ 
    path('Signup/',UserSignup,name='signup'),
    path('Login/',UserLogin,name='login'),



    #player
    path('player/profile',PlayerHome,name='playerhome'),

    # parent
    path('parent/profile',ParentHome,name='parenthome'),
]
