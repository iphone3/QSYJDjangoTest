from django.contrib import auth
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.shortcuts import render
from users.models import UserProfile
from django.views.generic.base import View

from utils.email_tool import send_email
from .forms import LoginForm,RegisterForm
from django.contrib.auth.hashers import make_password

# Create your views here.

# 自定义认证方法
class CustomBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            # 根据用户名或邮箱查找用户
            # user = UserProfile.objects.get(username=username)
            user = UserProfile.objects.get(Q(username=username) | Q(email=username))
            # 密码校验(密文)
            if user.check_password(password):
                return user
        except Exception as e:
            return None

# 登录
class LoginView(View):
    def get(self, request): # get请求
        return render(request, 'login.html', {})

    def post(self, request): # post请求
        # form组件，request.POST参数会对应到LoginForm中
        login_form = LoginForm(request.POST)
        if login_form.is_valid():   # 是否出错  【可以通过打断点的方式，看此处的参数等信息，其中会有一个errors】
            # 获取数据
            user_name = request.POST.get('username', '')
            pass_word = request.POST.get('password', '')

            # 用户验证
            user = auth.authenticate(request=request, username=user_name, password=pass_word)
            if user is not None:
                auth.login(request, user)  # 登录成功(处理了request，添加登录信息，其实就是cookie/session的封装)
                return render(request, 'index.html')
            else:
                return render(request, 'login.html', {'err_msg':'用户名或密码错误!'})
        else:   # 验证错误
            return render(request, 'login.html', {'login_form':login_form})

# 登录
# def login(request):
#     if request.method == 'POST':
#         # 获取数据
#         user_name = request.POST.get('username', '')
#         pass_word = request.POST.get('password', '')
#
#         # 用户验证
#         user = auth.authenticate(request=request, username=user_name, password=pass_word)
#         if user is not None:
#             auth.login(request, user)   # 登录成功(处理了request，添加登录信息，其实就是cookie/session的封装)
#             return render(request, 'index.html')
#         else:
#             return render(request, 'login.html', {'msg':'用户名或密码错误'})
#     elif request.method == 'GET':
#         return render(request, 'login.html', {})

# 注销
class LogoutView(View):
    def get(self, request):
        auth.logout(request)
        return render(request, 'index.html')


# 注册
class RegisterView(View):
    def get(self, request):
        register_form = RegisterForm()
        return render(request, 'register.html', {'register_form':register_form})

    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            # 获取数据
            username = request.POST.get('username', '')
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            password = request.POST.get('password', '')

            # 保存到数据库  【需要做验证处理】
            if UserProfile.objects.filter(username=username).exists():  # 用户名存在
                return render(request, 'register.html', {'username_err':'用户名已存在','register_form':register_form})
            elif UserProfile.objects.filter(email=email).exists():  # 邮箱存在
                return render(request, 'register.html', {'email_err':'邮箱已存在','register_form':register_form})
            else:   # 确保用户名和邮箱的唯一性，而不是存入数据库时报出异常
                user = UserProfile()
                user.username = username
                user.email = email
                user.nick_name = name
                # 加密处理
                user.password = make_password(password)
                user.save()

                # 发送激活链接【默认是没有被激活的】
                send_email(email)

                return render(request, 'login.html')
        else:
            return render(request, 'register.html', {'register_form':register_form})
