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
from goods.views import IndexView

urlpatterns = [
    url(r'^admin/', xadmin.site.urls),  # 后台
    url(r'^$', IndexView.as_view(), name='index'), # 首页
    url(r'^users/', include(('users.urls', 'users'), namespace='users')),  # users应用
    url(r'^goods/', include(('goods.urls', 'goods'), namespace='goods')),  # goods应用
    url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}), # 用户上传文件
    url(r'^captcha/', include('captcha.urls')),                     # 验证码 【注意该位置，不能有$结尾】
]