from django.contrib.messages.api import warning
from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from .forms import Signupform, LoginForm,userchangeform,PlayerUpdateForm,ParentUpdateForm
from Coach.forms import CoachUpdateForm
# Create your views here.
from Coach.models import CoachData
from django.contrib.auth import authenticate, forms, get_user_model
User = get_user_model()
from .models import ParentData,PlayerData
from django.contrib.auth import login,logout
from django.contrib import messages


def Courses(request):
    if request.user.is_authenticated and User.objects.get(username = request.user).UserType =="player":
        return render(request,'player/course.html')
    else :
        messages.error(request,"You don't have access to this page ")
        return HttpResponseRedirect('/')


def home(request):
    val = 0
    if request.user.is_authenticated:
        UserType = User.objects.get(username = request.user).UserType
        val = 1
        if UserType == "coach":
            val = 2
        elif UserType == "parent":
            val = 3
        
    return render(request,'main.html',{'UserType':val})


def PlayerHome(request):
    if request.user.is_authenticated and User.objects.get(username=request.user).UserType=="player":
        user = User.objects.get(username = request.user)
        player = PlayerData.objects.get(PlayerId= request.user)
        try :
            coach = CoachData.objects.get(CoachId = player.CoachName)
        except:
            coach = None
        context = {
            'player':player,
            'user':user,
            'coach':coach
        }
        return render(request,'player/profile.html',context)
    else :
        return HttpResponseRedirect('/')

# update user profile
def ViewPlayerProfile(request,pk):
    player = PlayerData.objects.get(pk=pk)
    
    context ={
        'player':player,
        
    }
    return render(request,'player/viewplayer.html',context);




# to be implemented 
def AddParentChild(request):
    pass

    # if request.method=="GET" and User.objects.get(username=request.GET['parent']).UserType=="parent":
    #     username = request.GET['username']
    #     try:
    #         user = get_object_or_404(User,username=username,UserType="player")
    #         parent = get_object_or_404(User, username = request.user)
    #         parent = ParentData.objects.get(ParentId=parent.id)
    #         parent.PlayerName = user.id
    #         parent.save()
    #         return JsonResponse({"status":200,"player":user.id})
    #     except:
    #         return JsonResponse({"status":200,"player":user.id})
    # else :
    #     return JsonResponse({"status":401})
    



def UserLogin(request):
    if not request.user.is_authenticated:
        if request.method =="POST":
            form = LoginForm(request,data = request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user =authenticate(username=username,password=password)
                if user:
                    login(request,user)
                    messages.success(request,f'Welcome back {username} ! Good to see you')
                    return HttpResponseRedirect('/')
                else:
                    messages.error(request,'User does not exist! Enter valid Credentials')
                    return HttpResponseRedirect(f'{request.META.get("HTTP_REFERER")}')
            else:
                messages.error(request,'User does not exist! Enter valid Credentials')
                return HttpResponseRedirect(f'{request.META.get("HTTP_REFERER")}')
        else :
            form = LoginForm()
        context = {
            'form':form,
            'formtype':'Login Form',
            'val':0,
        }
        return render(request,'auth/login.html',context)
    else:
        messages.error(request,"You are already logged in")
        return HttpResponseRedirect(f'{request.META.get("HTTP_REFERER")}')


def Userlogout(request):
    logout(request)
    messages.warning(request,"You have been logout !")
    return HttpResponseRedirect('/')


def EditProfile(request,id):
    if request.user.is_authenticated:
        if request.method == "POST":
            user = User.objects.get(pk=id)
            form1 = userchangeform(request.POST,instance = user)
            if user.UserType == "player":
                player = PlayerData.objects.get(PlayerId = request.user)
                form2 = PlayerUpdateForm(request.POST,instance=player)
            elif user.UserType == "coach":
                coach = CoachData.objects.get(CoachId = request.user)
                form2 = CoachUpdateForm(request.POST,instance=coach)
            elif user.UserType =="parent":
                parent = ParentData.objects.get(ParentId=request.user)
                form2 = ParentUpdateForm(request.POST,instance=parent)
            if form1.is_valid() and form2.is_valid():
                form1.save()
                form2.save()
                messages.success(request,"Profile updated successfully ")
                return HttpResponseRedirect(f'{request.META.get("HTTP_REFERER")}')
        else:
            form1 = userchangeform(instance = request.user)
            user = User.objects.get(username = request.user)
            if user.UserType == "player":
                player = PlayerData.objects.get(PlayerId = request.user)
                form2 = PlayerUpdateForm(instance=player)
            elif user.UserType == "coach":
                coach = CoachData.objects.get(CoachId = request.user)
                form2 = CoachUpdateForm(instance=coach)
            elif user.UserType =="parent":
                parent = ParentData.objects.get(ParentId=request.user)
                form2 = ParentUpdateForm(instance=parent)
        context = {
            'form1':form1,
            'form2':form2
        }
        return render(request,'auth/editprofile.html',context)
    else:
        messages.error(request,"You need to login to edit profile ")
        return HttpResponseRedirect(f'{request.META.get("HTTP_REFERER")}')
 
    

def UserSignup(request):
    if not request.user.is_authenticated:
        if request.method=="POST":
            form = Signupform(request.POST)
            print(form)
            if form.is_valid():
                UserType=form.cleaned_data['usertype']
                instance = form.save()
                instance.UserType = UserType
                instance.save()
                user = User.objects.get(username = form.cleaned_data['username'])
                if UserType=="coach":
                    coach = CoachData.objects.create(CoachId=user)
                    coach.save()
                elif UserType =="parent":
                    parent = ParentData.objects.create(ParentId=user)
                    parent.save()
                else :
                    player = PlayerData.objects.create(PlayerId=user)
                    player.save()
                messages.success(request,"Account Created! You may login")
                return HttpResponseRedirect('/')
            else:
                messages.error(request,"Please Enter Correct Details")
                return HttpResponseRedirect(f'{request.META.get("HTTP_REFERER")}')
        else :
            form = Signupform()
        context = {
            'form':form,
            'formtype':'Signup Form',
            'val':1,
        }
        return render(request,'auth/login.html',context)
    else:   
        messages.error(request,"Can't Signup While logging ! Be sure to logout first ")     
        return HttpResponseRedirect(f'{request.META.get("HTTP_REFERER")}')



