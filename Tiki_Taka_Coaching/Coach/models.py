from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.
class CoachData(models.Model):
    CoachId = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    CoachDetails = models.CharField(max_length=200)
    