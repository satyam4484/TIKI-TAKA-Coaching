from django.contrib import admin
from .models import CoachData
# Register your models here.
@admin.register(CoachData)
class CoachAdmin(admin.ModelAdmin):
    list_display=['CoachId','CoachDetails']