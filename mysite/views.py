from django.shortcuts import render
from mysite.models import Post
from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import redirect

# Create your views(程式邏輯) here. 
def homepage(request):#把資料準備好 再送去網頁 用網頁樣板去用資料 也是純文字
    posts = Post.objects.all()
    now = datetime.now()#時間
    return render(request,'index.html',locals())#(讀哪個檔案,把post加進locals())

def showpost(request,slug):#request浏览器向服务器发送的请求对象，包含用户信息、请求内容和请求方式等
    try:
        post = Post.objects.get(slug=slug)#找資料符合的 單一筆的 slug欄位取相對應的 兩個參數是因為在html定義的??
        if post!= None:
            return render(request,'post.html',locals())#前兩個是必要的
        else:
            return redirect("/")
    except:
        return redirect("/")#redirect轉網址
''' 
這個放到網頁上只有純文字 他只是存到list 然後放到網頁上
def homepage(request):#user透過網頁要做的事會被包成request傳進來
    posts = Post.objects.all()#會把資料庫的東西都傳出來
    post_lists = list()#動態陣列
    for counter,post in enumerate(posts):# counter,post(幾筆,資料)enumerate 會回傳兩個值(索引值跟資料)
        post_lists.append(f'No.{counter}-{post} <br>')#把東西加進去post_lists <br>是指換行
    return HttpResponse(post_lists)#得到的資料丟回去網路上(以純文字的方式)
'''