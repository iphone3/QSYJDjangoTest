from django.conf.urls import url
from .views import LoginView, LogoutView, RegisterView, ActiveView, ForgetView,ResetView

urlpatterns = [
    url(r'^login/$', LoginView.as_view(), name='login'),            # 登录
    url(r'^register/$', RegisterView.as_view(), name='register'),   # 注册
    url(r'^logout/$', LogoutView.as_view(), name='logout'),         # 退出
    url(r'^active/(?P<active_code>\w+)/$', ActiveView.as_view(), name='active'),    # 用户激活
    url(r'^forget/$', ForgetView.as_view(), name='forget'),         # 找回密码
    url(r'^reset/$', ResetView.as_view(), name='reset_sub'),        # 重置密码
    url(r'^reset/(?P<reset_code>\w+)/$', ResetView.as_view(), name='reset'), # 重置密码
]