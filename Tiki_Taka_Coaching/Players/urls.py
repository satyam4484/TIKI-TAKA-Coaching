from django.urls import path 
from .views import (UserSignup ,UserLogin,PlayerHome, Userlogout,ViewPlayerProfile,home,EditProfile,PlayerCourse,VedioDetails,ChangePasswordUser,AddParentChild)

urlpatterns = [ 
    path('',home,name='home'),
    path('Signup/',UserSignup,name='signup'),
    path('Login/',UserLogin,name='login'),
    path('logout/',Userlogout,name='logout'),
    path('changepassword/',ChangePasswordUser,name='changepassword'),
    path('editprofile/<int:id>',EditProfile,name='editprofile'),

    #player
    path('player/profile/',PlayerHome,name='playerhome'),
    path('player/viewprofile/<int:pk>',ViewPlayerProfile,name='playerprofile'),
    path('player/courses/',PlayerCourse,name='course'),
    path('player/vedios/<int:pk>',VedioDetails,name='vediodetails'),

    # parent
    path('parent/addplayer/',AddParentChild,name='addplayer')
]
