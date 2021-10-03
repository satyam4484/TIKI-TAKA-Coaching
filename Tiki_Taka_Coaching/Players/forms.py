# from django import forms 
from django.contrib.auth import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UserChangeForm

from django.contrib.auth import get_user_model
from django import forms
from django.forms import fields, models
from .models import PlayerData,ParentData
User = get_user_model()

class Signupform(UserCreationForm):
    usertype = forms.CharField(widget=forms.TextInput({'value':"player",'id':"usertype",'readonly':'','class':'form-control'}))
    username = forms.CharField(label='Username',label_suffix= ' ',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'user@123'}))
    password1 = forms.CharField(label='Password',label_suffix= ' ',widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'pass123'}))
    password2 = forms.CharField(label='Confirm Password',label_suffix= ' ',widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'pass123'}))
    class Meta:
        model = User 
        fields =['username','usertype']

class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Username',label_suffix= ' ',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'user@123','spellcheck':False,'autocorrect':'off','autocomplete':'off','autocapitalize':'off'}))
    password = forms.CharField(label='Password',label_suffix= ' ',widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'pass123','spellcheck':False,'autocorrect':'off','autocomplete':'off','autocapitalize':'off'}))
    class Meta:
        model = User
        fields = ['username','password']

class getdata(forms.Form):
    username = forms.CharField()
    class Meta:
        fields = ['username']


class userchangeform(UserChangeForm):
    username = forms.CharField(label='Username',label_suffix= ' ',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'user@123','spellcheck':False,'autocorrect':'off','autocomplete':'off','autocapitalize':'off'}))
    first_name=forms.CharField(label_suffix='',label='First Name ',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'First Name '}))
    last_name=forms.CharField(label_suffix='',label='Last Name',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Last Name '}))
    email=forms.EmailField(label_suffix='',label='Email',widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'user@gmail.com '}))
    usertype = forms.CharField(widget=forms.TextInput({'value':"player",'id':"usertype",'readonly':'','class':'form-control'}))
    password=None
    class Meta:
        model = User
        fields =['username','first_name','last_name','email','usertype']

class DateInput(forms.DateInput):
    input_type = 'date'


class PlayerUpdateForm(forms.ModelForm):
    PlayerCellNumber = forms.CharField(label_suffix='',label='Mobile Number',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'First Name '}))
    PlayerDob = forms.DateField(label='Date Of Birth',label_suffix='',widget=DateInput(attrs={'class':'form-control'}))
    class Meta:
        model = PlayerData
        fields = ['PlayerCellNumber','PlayerDob']

class ParentUpdateForm(forms.ModelForm):
    ParentDetails = forms.CharField(label_suffix='',label='Parent Details',widget=forms.Textarea(attrs={'class':'form-control'}))
    class Meta:
        model = ParentData
        fields = ['ParentDetails']

        



    