"""
URL configuration for mblog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views 函式的views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views 物件的views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from mysite import views as mv#匯入函式 也可以打成 form mysite.views import homepage
from mytest import views as testv
urlpatterns = [ #多打哪個網址會跑去哪
    path('admin/', admin.site.urls),#代表在網址後面打 admin會跑出啥
    path('',mv.homepage,name="homepage"),#網址啥都不打就先連到homepage這裡  如果上面import的方法改成備註的那樣 那這邊的逗號後面打homepage
    path('post/<slug:slug>/', mv.showpost, name="showpost"),#slug代表是變數(用<內容就是你在資料庫打的網址名稱>)  如果輸入post/.../就跑去那個函式
    path('post/', mv.show_all_posts, name="show_all_posts"),#中間的函式自己取(view裡面的class名字)
    path('about/', mv.about),#下面那個是字典的概念 如果沒定義就是放1 所以會回傳該陣列的[1]
    path('about/<int:num>',mv.about,{'num':1}),#num是變數名稱 型態是int 接收參數 在view那邊有設 如果你在about網址後面打999 下面h2也會跑999 ex:about/888 下面就有888
    path('post/<int:yr>/<int:mon>/<int:day>/<int:post_num>', mv.Post, name='post-url'),#如果驗證對了(驗證他的name) 他就會讓超連結的網址變125....
    path('carlist/', mv.carlist),
    path('carlist/<int:maker>/', mv.carlist, name='carlist-url'),#變數名字叫maker 去呼叫carlist個函式
    path('post/<int:post_id>/comments', mv.show_comments, name = 'show-comments'),#一對多的表格 可以定義slug或是用數字用 這裡的數字在html跑 後面再加上comments 顯示出所有的comments name是唯一的
    path('post/new',mv.new_post,name="post-new"),#看到post/new呼叫views的那個函式 post-new是給django呼叫的
    path('test',mv.homepage,name='test-name'),
    path('test/new',testv.index,name='test-name'),
    path('test/delpost/<int:pid>/',testv.delpost),
    path('test/contact',testv.contact),
    
]
