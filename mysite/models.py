from django.db import models
# Create your models here. 
class Post(models.Model):#定義物件  繼承models.Model 在資料庫建立post這個東西
    title = models.CharField(max_length=200)#字元
    slug = models.CharField(max_length=200)
    body = models.TextField()#長文字(不限制長度)
    category = models.TextField(null=True)#分類 是一個文字欄位 null=True多加欄位要允許他是空的 不然不能用
    pub_date = models.DateTimeField(auto_now_add=True)#時間 auto_now_add=True->自動取得時間
    
    class Meta:
        ordering = ('-pub_date', )#用時間排序 -是大到小 沒有-就是小到大
        
    def __str__(self):#__啥__ 是py內建的 這個是一個方法 就跟print很類似 它的型態是str
        return self.title#印出標題在資料庫裡面
    


class Comment(models.Model):#留言板 記得去admin讓它顯示
    post = models.ForeignKey(Post,on_delete=models.CASCADE)#他是主索引 然後他會到view的show_comments去抓資料
    text = models.CharField(max_length=200)#留言的欄位大小
    pub_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) :
        return self.text
    
    
class Product(models.Model):#在資料庫多一個 prduct這個東西 記得加到admin
    SIZES = (
        ('S', 'Small'),#前面是真正儲存的內容 後面是顯示的
        ('M', 'Medium'),
        ('L', 'Large'),
    )
    sku = models.CharField(max_length=5)
    name = models.CharField(max_length=20)
    price = models.PositiveIntegerField()
    size = models.CharField(max_length=1, choices=SIZES)#choices=SIZES 可以選擇size
    result = models.BooleanField()#新增一個欄位 但是在打makemigrate那兩行會錯 然後第一個輸入1(因為是布林 所以是1或0) 再來是0(word裡面有) 在打migrate的時候就可以了
    