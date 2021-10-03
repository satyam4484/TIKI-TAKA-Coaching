
from django.urls import path 

from .views import (UserSignup ,UserLogin,PlayerHome, Userlogout,ViewPlayerProfile,home,EditProfile,Courses)
from .parents import (ParentHome,AddParentChild)
urlpatterns = [ 
    path('',home,name='home'),
    path('Signup/',UserSignup,name='signup'),
    path('Login/',UserLogin,name='login'),
    path('logout/',Userlogout,name='logout'),
    path('editprofile/<int:id>',EditProfile,name='editprofile'),



    #player
    path('player/profile/',PlayerHome,name='playerhome'),
    path('viewprofile/<int:pk>',ViewPlayerProfile,name='playerprofile'),
    path('player/courses/',Courses,name='course'),


    # parent
    path('parent/profile/',ParentHome,name='parenthome'),
    path('parent/addplayer/',AddParentChild,name='addplayer')
]
