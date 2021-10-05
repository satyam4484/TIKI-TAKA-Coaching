from typing import Tuple
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    UserType = models.CharField(max_length=50)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.username}"
    
class PlayerData(models.Model):
    PlayerId = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    PlayerCellNumber=models.CharField(max_length=15,blank=True)
    PlayerDob = models.DateField(null=True,blank=True)
    CoachName = models.ForeignKey('Coach.CoachData',on_delete=models.CASCADE,null=True)
    score = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.PlayerId.username
    

class ParentData(models.Model):
    ParentId = models.OneToOneField(User,on_delete=models.CASCADE)
    PlayerName = models.OneToOneField(PlayerData,on_delete=models.CASCADE,null=True)
    ParentDetails = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.ParentId

    
