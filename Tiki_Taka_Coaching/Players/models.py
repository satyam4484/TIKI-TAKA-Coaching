from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_coach = models.BooleanField(default=False)
    is_parent = models.BooleanField(default=False)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
# class Player(models.Model):
#     PlayerId = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
#     PlayerCellNumber=models.CharField(max_length=15)
#     # PlayerDO


# class Parent(models.Model):
#     pass
