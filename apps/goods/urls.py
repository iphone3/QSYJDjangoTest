from django.conf.urls import url
from .views import IndexView, NurseView, ContactView, FavoriteView

urlpatterns = [
    url(r'^contact/$', ContactView.as_view(), name='contact'), # 彩瞳
    url(r'^nurse/$', NurseView.as_view(), name='nurse'), # 护理用品

    url(r'^favorite/$', FavoriteView.as_view(), name='favorite'),   # 用户收藏
]