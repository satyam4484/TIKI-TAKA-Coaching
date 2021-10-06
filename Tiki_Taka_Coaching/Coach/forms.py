from django import forms
from django.db import models
from django.db.models import fields 
from .models import CoachData,Category,VedioContent,VedioSubmission

class CoachUpdateForm(forms.ModelForm):
    CoachDetails = forms.CharField(label_suffix='',label='Coach Details',widget=forms.Textarea(attrs={'class':'form-control'}))
    CoachNumber = forms.CharField(label_suffix='',label='Mobile no',widget=forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model = CoachData
        fields = ['CoachDetails','CoachNumber']

class UploadVedio(forms.ModelForm):
    val=[]
    cat = Category.objects.all()
    for item in cat:
        val.append((item.id,item.CatName))
    val = tuple(val)
    category = forms.ChoiceField(label_suffix='',label='Select Week',choices=val,widget=forms.Select(attrs={'class':'form-control'}))
    VedioTitle = forms.CharField(label='Title',label_suffix='',widget=forms.TextInput(attrs={'class':'form-control'}))
    Desc = forms.CharField(label='Vedio Description',label_suffix='',widget=forms.Textarea(attrs={'class':'form-control'}))
    thumbnail = forms.ImageField(label_suffix='',label='Thumbnail',widget=forms.FileInput(attrs={'class':'form-control'}))
    vedio = forms.FileField(label_suffix='',label='Vedio',widget=forms.FileInput(attrs={'class':'form-control'}))
    class Meta:
        model = VedioContent
        fields= ['category','VedioTitle','Desc','thumbnail','vedio']
    def clean_category(self):
        category = self.cleaned_data['category']
        category = Category.objects.get(id = category)
        return category

class CategoryForm(forms.ModelForm):
    category = forms.CharField(label_suffix='',label='Enter Week',widget=forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model =Category
        fields = ['category']

class SubmitVedio(forms.ModelForm):
    UploadedVedio = forms.FileField(label_suffix='',label='Vedio',widget=forms.FileInput(attrs={'class':'form-control'}))

    class Meta:
        model = VedioSubmission
        fields = ['UploadedVedio']

class AssignMarks(forms.ModelForm):
    marks = forms.IntegerField(label='Grade',label_suffix='',widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Enter marks out of 10'}))
    class Meta:
        model = VedioSubmission
        fields= ['marks']