from django.contrib import auth
from django.contrib.auth.backends import ModelBackend
from django.core.cache import cache
from django.db.models import Q
from django.shortcuts import render, redirect
from users.models import UserProfile
from django.views.generic.base import View
from utils.email_tool import send_email
from .forms import LoginForm, RegisterForm, ForgetForm, ResetForm
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
                if user.is_active: # 激活状态
                    auth.login(request, user)  # 登录成功(处理了request，添加登录信息，其实就是cookie/session的封装)
                    return redirect('index')
                else:
                    # 如果超时，重新发送
                    send_email(user.username,user.email)
                    return render(request, 'login.html', {'err_msg':'用户未激活，请查看邮箱!'})
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
        return redirect('index')


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
                user.is_active = False  # 表示该用户未激活状态
                # 加密处理
                user.password = make_password(password)
                user.save()

                # 发送激活链接【默认是没有被激活的】
                send_email(user.username,email)

                # 提示用户，需要激活后登录
                return render(request, 'login.html', {'is_prompt': '请查看邮箱，激活后登录!'})
                # return render(request, 'login.html')
        else:
            return render(request, 'register.html', {'register_form':register_form})


# 激活
class ActiveView(View):
    def get(self, request, active_code):
        # 缓存有超时
        email = cache.get(active_code)
        if email:
            user = UserProfile.objects.get(email=email)
            user.is_active = True
            user.save()
            return render(request, 'login.html', {'is_prompt': '激活成功，请登录!'})
        else:
            return render(request, 'login.html', {'is_prompt': '已超时，请重新登录，再次发送邮件!'})

# 忘记密码
class ForgetView(View):
    def get(self, request):
        forget_form = ForgetForm()
        return render(request, 'forget.html', {'forget_form':forget_form})

    def post(self, request):
        forget_form = ForgetForm(request.POST)
        if forget_form.is_valid():
            email = request.POST.get('email')
            user = UserProfile.objects.filter(email=email).first()
            if user:
                send_email(user.username ,email, send_type=1)
                return render(request, 'login.html', {'is_prompt':'重置密码邮件已发出，请注意查收!'})
            else:
                return render(request, 'forget.html', {'forget_form': forget_form, 'err_msg':'邮箱不存在，请重新输入'})
        else:
            return render(request, 'forget.html', {'forget_form':forget_form})


# 重置密码
class ResetView(View):
    def get(self, request, reset_code):
        # 缓存有超时
        email = cache.get(reset_code)
        if email:
            # 得传入email，后续再重置密码时，带入才知道是哪个用户重置密码
            return render(request, 'reset.html', {'email':email})
        else:
            forget_form = ForgetForm()
            return render(request, 'forget.html', {'is_prompt': '重置链接已超时，请重新提交!', 'forget_form':forget_form})

    def post(self, request):
        reset_form = ResetForm(request.POST)
        if reset_form.is_valid():
            pwd1 = request.POST.get('password1', '')
            pwd2 = request.POST.get('password2', '')
            email = request.POST.get('email')
            if pwd1 != pwd2:
                return render(request, 'reset.html', {'email':email, 'err_msg':'两次密码输入不一致'})

            user = UserProfile.objects.get(email=email)
            user.password = make_password(pwd1)
            user.save()

            return render(request, 'login.html', {'is_prompt': '重置密码成功!'})
        else:
            email = request.POST.get('email')
            return render(request, 'reset.html', {'email': email, 'err_msg': '密码长度错误，注意是6~12位'})
