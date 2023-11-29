from django.contrib import admin
from mysite.models import Post,Product,Comment#匯入物件
# Register your models here.

class PostAdmin(admin.ModelAdmin):#管理者的物件
    list_display = ('id', 'title','slug','pub_date')#讓管理者可以看到這三個介面
    
    
class CommentAdmin(admin.ModelAdmin):#管理者的物件
    list_display = ('text','pub_date')#可以看product跟這兩個的差別

admin.site.register(Post, PostAdmin)#把你要註冊到管理者網站的東西放()內
admin.site.register(Product)#如果要真正有欄位要打這行
admin.site.register(Comment, CommentAdmin)