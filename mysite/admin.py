from django.contrib import admin
from mysite.models import Post#匯入物件
# Register your models here.

class PostAdmin(admin.ModelAdmin):#管理者的物件
    list_display = ('title','slug','pub_date')#讓管理者可以看到這三個介面
    
admin.site.register(Post, PostAdmin)#把你要註冊到管理者網站的東西放()內
