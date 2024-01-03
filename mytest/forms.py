from django import forms#表單推薦用這種寫法 ppt50幾頁
from mytest import models
from mytest.models import Post  
class ContactForm(forms.Form):#forms就是在定義欄位的概念 到view才是真正的看要存甚麼
    CITY = [
        ['TP', 'Taipei'],
        ['TY', 'Taoyuang'],
        ['TC', 'Taichung'],
        ['TN', 'Tainan'],
        ['KS', 'Kaohsiung'],
        ['NA', 'Others'],
    ]
    user_name = forms.CharField(label='您的姓名', max_length=50, initial='李大仁')#initial 初始直
    user_city = forms.ChoiceField(label='居住城市', choices=CITY)#這是下拉式選單 choices的city是從上面來的
    user_school = forms.BooleanField(label='是否在學', required=False)#核取方塊
    user_email = forms.EmailField(label='電子郵件')
    user_message = forms.CharField(label='您的意見', widget=forms.Textarea)#widget=forms.Textarea字串欄位顯示成怎樣

class PostForm(forms.ModelForm):#表單會連到資料庫
    class Meta:#跟哪個資料庫相關
        model = models.Post#會連到資料庫的Post裡面
        fields = ['mood', 'nickname', 'message', 'del_pass']#定義要儲存欄位(要跟上面的一樣就是要跟Post有關聯)
    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['mood'].label = '現在心情'#有引用到model的mood
        self.fields['nickname'].label = '你的暱稱'#預設值在model
        self.fields['message'].label = '心情留言'
        self.fields['del_pass'].label = '設定密碼'

class UserRegisterForm(forms.Form):
    user_name = forms.CharField(label='您的帳號', max_length=50, initial='ericlai')#
    user_email = forms.EmailField(label='電子郵件')
    user_password = forms.CharField(label='輸入密碼', widget=forms.PasswordInput)#
    user_password_confirm = forms.CharField(label='輸入確認密碼', widget=forms.PasswordInput)#

class  LoginForm(forms.Form):
    user_name = forms.CharField(label='您的帳號', max_length=50, initial='ericlai')#
    user_password = forms.CharField(label='輸入密碼', widget=forms.PasswordInput)#
    
class ProfileForm(forms.ModelForm):
    class Meta:
        model = models.Profile#跟哪個資料庫相關
        fields = ['height', 'male', 'website']#定義要儲存欄位(要跟上面的一樣就是要跟Post有關聯)
    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.fields['height'].label = '身高'#有引用到model的mood
        self.fields['male'].label = '性別'#預設值在model
        self.fields['website'].label = '個人網址'