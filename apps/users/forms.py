from django import forms
from captcha.fields import CaptchaField

# 登录操作验证
class LoginForm(forms.Form):
    # 定义(注意字段和模板input中name属性保持一致，否则获取不到数据验证)
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, max_length=12, min_length=6)


# 注册验证
class RegisterForm(forms.Form):
    username = forms.CharField(required=True, max_length=12, min_length=3)   # 用户名
    name = forms.CharField(required=True)       # 昵称
    email = forms.CharField(required=True)
    password = forms.CharField(required=True,max_length=12, min_length=6)
    # 定制错误信息，会抛出一个invalid异常 【key要注意书写】
    captcha = CaptchaField(error_messages={'invalid':'验证码错误'})    # 验证码


