# from django import forms 
from django.contrib.auth import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm

from django.contrib.auth import get_user_model
from django import forms
User = get_user_model()

class Signupform(UserCreationForm):
    usertype = forms.CharField(widget=forms.TextInput({'value':"player",'id':"usertype",'readonly':''}))
    class Meta:
        model = User 
        fields =['username','usertype']

class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username','password']