from django.shortcuts import render
from mysite.models import Post
from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import redirect

# Create your views(程式邏輯) here. 
def homepage(request):#把資料準備好 再送去網頁 用網頁樣板去用資料 也是純文字
    posts = Post.objects.all()
    now = datetime.now()#時間
    hour = now.timetuple().tm_hour
    return render(request,'index.html',locals())#(讀哪個檔案,用local方式打包)

def showpost(request,slug):#request浏览器向服务器发送的请求对象，包含用户信息、请求内容和请求方式等
    try:
        post = Post.objects.get(slug=slug)#是從數據庫取得一個匹配的結果 返回一個對象 如果紀錄不存在的話 會回復錯誤
        if post!= None:
            return render(request,'post.html',locals())#前兩個是必要的 locals 把區域網路的東西打包
        else:
            return redirect("/")
    except:
        return redirect("/")#redirect轉網址 如果產生錯誤就回到首頁
import random    
def about(request, num=-1):#request一定要寫 num是自己先預設基本參數 可以負責接收參數
    quotes = ['今日事，今日畢',
                '要怎麼收穫，先那麼栽',
                '知識就是力量',
                '一個人的個性就是他的命運']
    if num==-1 or num>4:
        quote = random.choice(quotes)
        return render(request, 'about.html', locals()) 
    else:
        quote=quotes[num]#取你輸入的數字所指定到的 陣列裡面的字
        return  render(request, 'about.html', locals()) 
    
def carlist(request, maker=0):
    car_maker = ['Ford', 'Honda', 'Mazda']#如果點SAAB 裡面就沒東西 點Ford就會跑出第二個陣列 搭配html去看
    car_list =  [
        [{'model':'Fiesta', 'price': 203500},
            {'model':'Focus','price': 605000},
            {'model':'Mustang','price': 900000}],
		[{'model':'Fit', 'price': 450000}, 
		 {'model':'City', 'price': 150000}, 
		 {'model':'NSX', 'price':1200000}],
		[{'model':'Mazda3', 'price': 329999}, 
		 {'model':'Mazda5', 'price': 603000},
		 {'model':'Mazda6', 'price':850000}],
        ]


	
    maker = maker
    maker_name =  car_maker[maker]
    cars = car_list[maker]
    return render(request, 'carlist.html', locals())

''' 
這個放到網頁上只有純文字 他只是存到list 然後放到網頁上
def homepage(request):#user透過網頁要做的事會被包成request傳進來
    posts = Post.objects.all()#會把資料庫的東西都傳出來
    post_lists = list()#動態陣列
    for counter,post in enumerate(posts):# counter,post(幾筆,資料)enumerate 會回傳兩個值(索引值跟資料)
        post_lists.append(f'No.{counter}-{post} <br>')#把東西加進去post_lists <br>是指換行
    return HttpResponse(post_lists)#得到的資料丟回去網路上(以純文字的方式)
'''