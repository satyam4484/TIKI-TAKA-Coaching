from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import get_user_model
User = get_user_model()
from Players.models import PlayerData
from .models import CoachData,Category,VedioContent
from .forms import UploadVedio
from django.contrib import messages
# Create your views here.

def CoachProfile(request):
    if request.user.is_authenticated and User.objects.get(username=request.user).UserType=="coach":
        PendingPlayer = PlayerData.objects.filter(CoachName = None)
        Trainingplayers = PlayerData.objects.filter(CoachName = request.user.id).order_by('-Rank');
        user = User.objects.get(username= request.user)
        coach = CoachData.objects.get(CoachId = user.id)
        if request.method == "POST":
            form = UploadVedio(request.POST,request.FILES)
            if form.is_valid():
                week = form.cleaned_data['category']
                print(week)
                # instance = form.save(commit=False)
                # instance.user = request.user
                # instance.save()
                messages.success(request,"Vedio uploaded successfully")
                # return HttpResponseRedirect(f'{request.META.get("HTTP_REFERER")}')
        else:
            form = UploadVedio()
        # -------------------------------------------------------------------

        vedios=[]
        category = Category.objects.values()
        for cat in category:
            vedio = VedioContent.objects.filter(category=cat['id'],author=request.user.id)
            content = []
            for items in vedio:
                content.append(items)
            val = {f'{cat["CatName"]}':content}
            vedios.append(val)

        print(vedios)       
        context = {
            'pendingplayer':PendingPlayer,
            'Trainingplayer':Trainingplayers,
            'user':user,
            'coach':coach,
            'form':form,
            'vedios':vedios
        }
        return render(request,'coach/profile.html',context)
    else :
        return HttpResponseRedirect('/')

def DeleteVedio(request,pk):
    vedio = VedioContent.objects.get(pk=pk)
    vedio.delete()
    messages.success(request,"vedio deleted successfully")
    return HttpResponseRedirect(f'{request.META.get("HTTP_REFERER")}') 
'''
[
    {'Week1': [
        {'id': 1, 'VedioTitle': 'Testing', 'Desc': 'Testing vedio to view', 'vedio': 'vedios/<django.db.models.fields.related.ForeignKey>/2020-Ganpati-Bappa-WhatsApp-Status-Video.mp4'}
        ]
    },
    
    {'Week2': [{'id': 2, 'VedioTitle': 'Testing12', 'Desc': 'new week vedio', 'vedio': 'vedios/<django.db.models.fields.related.ForeignKey>/2020-Ganpati-Bappa-WhatsApp-Status-V_iyHxANY.mp4'}]}
]

'''

def TrainPlayer(request,pk):
    if request.user.is_authenticated and User.objects.get(username=request.user).UserType=="coach":
        print("inside");
        player = PlayerData.objects.get(PlayerId__id =pk)
        player.CoachName = CoachData.objects.get(CoachId=request.user)
        player.save()
        return HttpResponseRedirect(f'{request.META.get("HTTP_REFERER")}')
    else :
        return HttpResponseRedirect(f'{request.META.get("HTTP_REFERER")}')

