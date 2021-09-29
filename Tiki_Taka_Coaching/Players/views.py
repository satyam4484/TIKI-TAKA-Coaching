from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import Signupform, LoginForm
# Create your views here.
from Coach.models import CoachData
from django.contrib.auth import authenticate, get_user_model
User = get_user_model()
from .models import ParentData,PlayerData
from django.contrib.auth import login,logout



def PlayerHome(request):
    if request.user.is_authenticated and User.objects.get(username=request.user).UserType=="player":
        return render(request,'player/profile.html')
    else :
        return HttpResponseRedirect('/')


# parent

def ParentHome(request):
    if request.user.is_authenticated and User.objects.get(username=request.user).UserType=="parent":
        return render(request,'parents/profile.html')
    else :
        return HttpResponseRedirect('/')





def UserLogin(request):
    if request.method =="POST":
        form = LoginForm(request,data = request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user =authenticate(username=username,password=password)
            if user:
                login(request,user)
                return HttpResponseRedirect('/')
    else :
        form = LoginForm()
    context = {
        'form':form
    }
    return render(request,'auth/login.html',context)


def Userlogout(request):
    pass

def EditProfile(request,id):
    pass

def UserSignup(request):
    if request.method=="POST":
        form = Signupform(request.POST)
        print(form)
        if form.is_valid():
            usertype=form.cleaned_data['usertype']
            instance = form.save()
            instance.UserType = usertype
            instance.save()
            user = User.objects.get(username = form.cleaned_data['username'])
            if usertype=="coach":
                coach = CoachData.objects.create(CoachId=user)
                coach.save()
            elif usertype =="parent":
                parent = ParentData.objects.create(ParentId=user)
                parent.save()
            else :
                player = PlayerData.objects.create(PlayerId=user)
                player.save()
            return HttpResponseRedirect('/')
    else :
        form = Signupform()
    context = {
        'form':form,
    }
    return render(request,'auth/signup.html',context)


