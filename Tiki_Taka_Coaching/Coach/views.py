from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your views here.
def CoachProfile(request):
    if request.user.is_authenticated and User.objects.get(username=request.user).UserType=="coach":
        return render(request,'coach/profile.html')
    else :
        return HttpResponseRedirect('/')