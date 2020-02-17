from django import forms

# 登录操作
class LoginForm(forms.Form):
    # 定义(注意字段和模板input中name属性保持一致，否则获取不到数据验证)
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, max_length=12, min_length=6)
