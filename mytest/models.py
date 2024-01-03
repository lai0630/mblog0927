from django.db import models


class Mood(models.Model):#下拉式選單
    status = models.CharField(max_length=10, null=False)

    def __str__(self):
        return self.status

class Post(models.Model):
    mood = models.ForeignKey('Mood', on_delete=models.CASCADE)
    nickname = models.CharField(max_length=10, default='不願意透漏身份的人')
    message = models.TextField(null=False)
    del_pass = models.CharField(max_length=10)
    pub_time = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=True)#預設讓他做顯示
    
    def __str__(self):
        return self.message

from django.contrib import auth

class Profile(models.Model):
    user = models.OneToOneField(auth.models.User, on_delete=models.CASCADE)#一對一的欄位 指到的欄位是auth.models.User(內建的)
    height = models.PositiveIntegerField(default=160)
    male = models.BooleanField(default=False)
    website = models.URLField(null=True)
	
    def __str__(self):
        return self.user.username
