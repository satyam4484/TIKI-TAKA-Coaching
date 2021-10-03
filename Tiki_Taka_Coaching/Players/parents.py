from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from .forms import Signupform, LoginForm,getdata
# Create your views here.
from Coach.models import CoachData
from django.contrib.auth import authenticate, get_user_model
User = get_user_model()
from .models import ParentData,PlayerData
from django.contrib.auth import login,logout

def AddParentChild(request):
    pass

def ParentHome(request):
    if request.user.is_authenticated and User.objects.get(username = request.user).UserType =="parent":
        
        return render(request,'parents/profile.html')
    else:
        return HttpResponseRedirect('/')