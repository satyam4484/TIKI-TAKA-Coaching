from django.conf.urls import url
from django.urls import path 

from .views import CoachProfile
urlpatterns = [
    path('profile/',CoachProfile,name='coachprofile'),
    
]
