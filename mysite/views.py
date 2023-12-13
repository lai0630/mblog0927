from django.shortcuts import render
from mysite.models import Post,Comment
from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import redirect

# Create your views(程式邏輯) here. 
def homepage(request):#把資料準備好 再送去網頁 用網頁樣板去用資料 也是純文字
    posts = Post.objects.all()
    now = datetime.now()#時間
    hour = now.timetuple().tm_hour
    years = range(1960,2024)
    return render(request,'index.html',locals())#(讀哪個檔案,用local方式打包)

def show_all_posts(request):
    posts = Post.objects.all()#顯示全部
    return render(request, 'allposts.html', locals())


def showpost(request,slug):#request浏览器向服务器发送的请求对象，包含用户信息、请求内容和请求方式等
    try:
        post = Post.objects.get(slug=slug)#是從數據庫取得一個匹配的結果 返回一個對象 如果紀錄不存在的話 會回復錯誤
        if post!= None:
            return render(request,'post.html',locals())#前兩個是必要的 locals 把區域網路的東西打包
        else:
            return redirect("/")
    except:
        return redirect("/")#redirect轉網址 如果產生錯誤就回到首頁

def show_comments(request,post_id):#如果urls有參數 那這邊就要有參數
    #comments = Comment.objects.filter(post=post_id)#抓多筆是這個
    comments = Post.objects.get(id=post_id).comment_set.all()#get只能抓一筆資料 comment_set.all是動態產生的(明明沒寫 他會幫你產生)把資料自動往下抓(一對多)
    return render(request, 'comments.html', locals())
    
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
    car_maker = ['Ford', 'Honda', 'Mazda']#如果點Ford就會跑出第一個陣列 點Honda會跑第二個陣列搭配html去看
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

from django.http import HttpResponseRedirect
from django.urls import reverse
def new_post(request):#存到資料庫的東西
    print(f'form method:{request.method}')
    if request.method=='GET':#method="post"看表單上(form那邊)的方法是get還是post
        return render(request, 'myform_1.html', locals())
    elif request.method=='POST':#都要全大寫
        title = request.POST['title']#跟html裡面的你要抓的那個欄位的name一樣
        slug = request.POST['slug']#如果改成post前面就要全大寫的POST
        content = request.POST['content']
        category = request.POST.getlist('category')#會把該html相對名字的東西全部抓去後端(是一個串列) 記得是用 ()
        post = Post(title=title,slug=slug,body=content,category=category)#會讓他跑到models中的Post 然後Post的title = 我們在網頁打的title(裡面的字)....
        post.save()#如果在上面打完後可以直接儲存到資料庫 他就會跟你在admin裡面打得一模一樣
        return render(request,'myform_1.html',locals())#HttpResponseRedirect重新導向到urls的name叫做show all posts的地方
        #return render(request, 'myform_1.html', locals())#locals()->把裡面的東西都變成local 然後讓網頁可以用


    '''
    try:
        username = request.GET['user_id']#跟html裡面的你要抓的那個欄位的name一樣
        password = request.GET['password']
        print(f'username:{username}, password:{password}')#cmd那邊會出現
        return render(request, 'myform_1.html', locals())
    except:
        return render(request, 'myform_1.html', locals())#如果在http那邊第一行是用get 那就是用render
''' 
'''
這個放到網頁上只有純文字 他只是存到list 然後放到網頁上
def homepage(request):#user透過網頁要做的事會被包成request傳進來
    posts = Post.objects.all()#會把資料庫的東西都傳出來
    post_lists = list()#動態陣列
    for counter,post in enumerate(posts):# counter,post(幾筆,資料)enumerate 會回傳兩個值(索引值跟資料)
        post_lists.append(f'No.{counter}-{post} <br>')#把東西加進去post_lists <br>是指換行
    return HttpResponse(post_lists)#得到的資料丟回去網路上(以純文字的方式)
'''