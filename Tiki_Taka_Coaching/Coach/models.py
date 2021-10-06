from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
from Players.models import PlayerData
# Create your models here.
class CoachData(models.Model):
    CoachId = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    CoachDetails = models.CharField(max_length=200)
    CoachNumber = models.CharField(max_length=15,unique=True)
    
    def __str__(self) -> str:
        return self.CoachId.username

# category table 
class Category(models.Model):
    CatName = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.CatName

# vedio table 
class VedioContent(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    VedioTitle = models.CharField(max_length=200)
    author = models.ForeignKey(CoachData,on_delete=models.CASCADE,null=True,blank=True)
    Desc = models.TextField()
    thumbnail = models.ImageField(upload_to="images/%y")
    vedio = models.FileField(upload_to="vedio/%y")
   

    def __str__(self) -> str:
        return self.VedioTitle

# submission vedio table 
class VedioSubmission(models.Model):
    vedio = models.ForeignKey(VedioContent,on_delete=models.CASCADE)
    player = models.ForeignKey(PlayerData,on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    UploadedVedio = models.FileField(upload_to='upload/%y')
    marks = models.IntegerField(null=True,blank=True)
    submit = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.player} uploaded vedio to coach {self.vedio.author} on {self.date}'

