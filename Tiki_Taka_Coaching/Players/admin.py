from django.contrib import admin
from .models import User,ParentData,PlayerData

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display=['id','username','email','first_name','last_name','UserType','is_active','is_staff','is_superuser']

@admin.register(PlayerData)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ['PlayerId','PlayerCellNumber','PlayerDob','CoachName','score']


@admin.register(ParentData)
class ParentAdmin(admin.ModelAdmin):
    list_display = ['ParentId']
    