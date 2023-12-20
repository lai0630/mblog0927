from django import forms#表單推薦用這種寫法 ppt50幾頁
from mytest import models
from mytest.models import Post  
class ContactForm(forms.Form):
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
        fields = ['mood', 'nickname', 'message', 'del_pass']#規定欄位
        