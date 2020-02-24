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

import xadmin
from django.views.generic import TemplateView
from users.views import LoginView, LogoutView, RegisterView, ActiveView

urlpatterns = [
    url(r'^admin/', xadmin.site.urls),
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='index'), # 首页
    url(r'^login/$', LoginView.as_view(), name='login'),   # 登录
    url(r'^register/$', RegisterView.as_view(), name='register'),   # 注册
    url(r'^logout/$', LogoutView.as_view(), name='logout'),   # 退出
    url(r'^captcha/', include('captcha.urls')),    # 验证码 【注意该位置，不能有$结尾】
    url(r'^active/(?P<active_code>\w+)/$', ActiveView.as_view(), name='active'),    # 用户激活
]
