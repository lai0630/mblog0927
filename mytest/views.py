from django.shortcuts import render
from mytest.models import Post, Mood
from django.shortcuts import redirect
from mytest.forms import ContactForm,PostForm,UserRegisterForm,LoginForm

def index(request): 
    posts = Post.objects.filter(enabled=True).order_by('-pub_time')[:30]#[:30]取前三十個  order_by('pub_date')用日期來排序
    moods = Mood.objects.all()#把東西從資料庫抓出來
    if request.method == 'GET':
        return render(request,'myform.html',locals())#一定要回應
    elif request.method =='POST':
        try:
            user_id = request.POST['user_id']
            user_pass = request.POST['user_pass']
            user_post = request.POST['user_post']
            user_mood = request.POST['mood']
            mood = Mood.objects.get(status=user_mood)
            post = Post(mood=mood, nickname=user_id, del_pass=user_pass, message=user_post)#先把物件綁定到post裡面
            post.save()#讓他存到資料庫裏面
            message = '成功儲存！請記得你的編輯密碼[{}]!，訊息需經審查後才會顯示。'.format(user_pass)
            return render(request,'myform.html',locals())#一定要回應
        except Exception as e:
            print(e)
            message = '出現錯誤'
            return render(request,'myform.html',locals())#一定要回應
    else:
            message = 'post/get 出現錯誤'
            return render(request,'myform.html',locals())#一定要回應

def delpost(request,pid):#pid對應到前面urls的
    if pid:
        try:
            post = Post.objects.get(id=pid)
            post.delete()
        except:
            print('刪除錯誤 pid=',pid)
            pass
    return redirect('/test')

def contact(request):#做一個form.py
    if request.method == 'GET':
        form = ContactForm()
        return render(request,'myContact.html',locals())#一定要回應
    elif request.method =='POST':
        form = ContactForm(request.POST)#去request抓資料 把變數抓下來
        if form.is_valid():#一定要寫這個(if以下的)才能抓值 這個是要抓裡面的值
            user_name = form.cleaned_data['user_name']
            user_message = form.cleaned_data['user_message']
            print('user_name:',user_name)   
        return render(request,'myContact.html',locals())#一定要回應
    else:
        massge='ERROR'
        return render(request,'myContact.html',locals())#一定要回應
    
def post2db(request):#用這種
    if request.method == 'GET':
        form = PostForm()
        return render(request,'myPost2DB.html',locals())#一定要回應
    elif request.method =='POST':
        form = PostForm(request.POST)#去request抓資料 把變數抓下來
        if form.is_valid():#一定要寫這個(if以下的) 這個是要抓裡面的值
            form.save()  #這邊可以存是因為他在forms已經定義好了 不然要像18 19那行
        return render(request,'myPost2DB.html',locals())#一定要回應
    else:
        massge='ERROR'
        return render(request,'myPost2DB.html',locals())#一定要回應
 
from django.contrib.auth.models import User
   
def register(request):#會直接存到這個程式的資料庫 而不是admin
    if request.method == 'GET':
        form = UserRegisterForm()
        return render(request,'register.html',locals())#一定要回應
    elif request.method =='POST':
        form = UserRegisterForm(request.POST)#去request抓資料 把變數抓下來
        if form.is_valid():#一定要寫這個(if以下的) 這個是要抓裡面的值
            user_name = form.cleaned_data['user_name']
            user_email = form.cleaned_data['user_email']
            user_password = form.cleaned_data['user_password']
            user_password_confirm = form.cleaned_data['user_password_confirm']
            if user_password == user_password_confirm:
                user = User.objects.create_user(user_name,user_email,user_password)#有名字email password 密碼會加密
                message=f'註冊成功'
            else:
                message=f'兩次密碼不一樣'
        return render(request,'register.html',locals())#一定要回應
    else:
        massge='ERROR'
        return render(request,'register.html',locals())#一定要回應

from django.contrib.auth import authenticate
from django.contrib import auth
from django.contrib.auth.decorators import login_required
def login (request):
    if request.method == 'GET':
        form = LoginForm()#代表會顯示的欄位 在forms那邊
        return render(request,'login.html',locals())#一定要回應
    elif request.method =='POST':
        form = LoginForm(request.POST)#去request抓資料 把變數抓下來
        if form.is_valid():#一定要寫這個(if以下的) 這個是要抓裡面的值
            user_name = form.cleaned_data['user_name']
            user_password = form.cleaned_data['user_password']
            user = authenticate(username=user_name, password=user_password)
            if user is not None:
                if user.is_active:
                    auth.login(request, user)
                    print("success")
                    message='成功'
                    return redirect('/')
                else:
                    message='未啟用'
            else:
                message='失敗'
        return render(request,'login.html',locals())#一定要回應
    else:
        massge='ERROR'
        return render(request,'login.html',locals())#一定要回應
