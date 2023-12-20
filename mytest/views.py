from django.shortcuts import render
from mytest.models import Post, Mood
from django.shortcuts import redirect
from mytest.forms import ContactForm

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

def contact(request):
    if request.method == 'GET':
        form = ContactForm()
        return render(request,'myContact.html',locals())#一定要回應
    elif request.method =='POST':
        form = ContactForm(request.POST)#去request抓資料 把變數抓下來
        if form.is_valid():#一定要寫這個(if以下的) 這個是要抓裡面的值
            user_name = form.cleaned_data['user_name']
            user_message = form.cleaned_data['user_message']
            print('user_name:',user_name)   
        return render(request,'myContact.html',locals())#一定要回應
    else:
        massge='ERROR'
        return render(request,'myContact.html',locals())#一定要回應