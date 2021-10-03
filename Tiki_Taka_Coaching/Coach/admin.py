from django.contrib import admin
from .models import CoachData,Category,VedioContent,VedioSubmission
# Register your models here.
@admin.register(CoachData)
class CoachAdmin(admin.ModelAdmin):
    list_display=['CoachId','CoachDetails']

admin.site.register(Category)

@admin.register(VedioContent)
class VedioAdmin(admin.ModelAdmin):
    list_display = ['id','category','VedioTitle','Desc','thumbnail','vedio']

@admin.register(VedioSubmission)
class SubmissionAdmin(admin.ModelAdmin):
    list_display=['id','vedio','player','date','UploadedVedio','marks']
    