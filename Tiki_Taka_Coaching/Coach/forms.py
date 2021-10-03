from django import forms
from django.db.models import fields 
from .models import CoachData,Category,VedioContent

class CoachUpdateForm(forms.ModelForm):
    CoachDetails = forms.CharField(label_suffix='',label='Coach Details',widget=forms.Textarea(attrs={'class':'form-control'}))
    CoachNumber = forms.CharField(label_suffix='',label='Mobile no',widget=forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model = CoachData
        fields = ['CoachDetails','CoachNumber']


val=[]
cat = Category.objects.all()
for item in cat:
    val.append((item.id,item.CatName))
val = tuple(val)


class UploadVedio(forms.ModelForm):
    category = forms.ChoiceField(label_suffix='',label='Select Week',choices=val,widget=forms.Select(attrs={'class':'form-control'}))
    VedioTitle = forms.CharField(label='Title',label_suffix='',widget=forms.TextInput(attrs={'class':'form-control'}))
    Desc = forms.CharField(label='Vedio Description',label_suffix='',widget=forms.Textarea(attrs={'class':'form-control'}))
    thumbnail = forms.ImageField(label_suffix='',label='Thumbnail',widget=forms.FileInput(attrs={'class':'form-control'}))
    vedio = forms.FileField(label_suffix='',label='Vedio',widget=forms.FileInput(attrs={'class':'form-control'}))
    class Meta:
        model = VedioContent
        fields= ['category','VedioTitle','Desc','thumbnail','vedio']