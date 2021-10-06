from django.conf.urls import url
from django.urls import path 

from .views import CoachProfile,TrainPlayer,DeleteVedio,WatchSubmission,AddCategory
urlpatterns = [
    path('profile/',CoachProfile,name='coachprofile'),
    path('addplayer/<int:pk>',TrainPlayer,name='trainplayer'),
    path('deletevedio/<int:pk>',DeleteVedio,name='deletevedio'),    
    path('watch/<int:pk>',WatchSubmission,name='watchsubmission'),
    path('cat/',AddCategory,name='category'),
]
