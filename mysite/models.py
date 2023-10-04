from django.db import models
# Create your models here. 
class Post(models.Model):#定義物件  繼承models.Model
    title = models.CharField(max_length=200)#字元
    slug = models.CharField(max_length=200)
    body = models.TextField()#長文字(不限制長度)
    pub_date = models.DateTimeField(auto_now_add=True)#時間 auto_now_add=True->自動取得時間
    
    class Meta:
        ordering = ('-pub_date', )#用時間排序 -是大到小 沒有-就是小到大
        
    def __str__(self):#__啥__ 是py內建的 這個是一個方法 就跟print很類似 它的型態是str
        return self.title#印出標題