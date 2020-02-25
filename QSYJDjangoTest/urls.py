"""QSYJDjangoTest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.urls import include
from django.views.static import serve

import xadmin
from django.views.generic import TemplateView

from QSYJDjangoTest.settings import MEDIA_ROOT
from goods.views import IndexView,NurseView,ContactView
from users.views import LoginView, LogoutView, RegisterView, ActiveView, ForgetView,ResetView

urlpatterns = [
    url(r'^admin/', xadmin.site.urls),  # 后台

    url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}), # 用户上传文件

    url(r'^$', IndexView.as_view(), name='index'), # 首页
    url(r'^contact/$', ContactView.as_view(), name='contact'), # 彩瞳
    url(r'^nurse/$', NurseView.as_view(), name='nurse'), # 护理用品

    url(r'^login/$', LoginView.as_view(), name='login'),            # 登录
    url(r'^register/$', RegisterView.as_view(), name='register'),   # 注册
    url(r'^logout/$', LogoutView.as_view(), name='logout'),         # 退出
    url(r'^captcha/', include('captcha.urls')),                     # 验证码 【注意该位置，不能有$结尾】
    url(r'^active/(?P<active_code>\w+)/$', ActiveView.as_view(), name='active'),    # 用户激活
    url(r'^forget/$', ForgetView.as_view(), name='forget'),         # 找回密码
    url(r'^reset/$', ResetView.as_view(), name='reset_sub'),        # 重置密码
    url(r'^reset/(?P<reset_code>\w+)/$', ResetView.as_view(), name='reset'), # 重置密码
]
