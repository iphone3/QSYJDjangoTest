import xadmin
from users.models import UserProfile
from xadmin import views


# xadmin主题
class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True
xadmin.site.register(views.BaseAdminView, BaseSetting)

# xadmin全局配置
class GlobalSettings(object):
    """系统信息"""
    site_title = "全视眼镜商城"  # 左上角信息
    site_footer = "技术支持: zyz"  # 下方信息
    menu_style = "accordion"  # 收起侧边栏
xadmin.site.register(views.CommAdminView, GlobalSettings)


# class EmailVerifyRecordAdmin(object):
#     # 后台显示字段
#     list_display = ['code', 'email', 'send_type', 'send_time']
#     # 搜索字段
#     search_fields = ['code', 'email', 'send_type']
#     # 字段过滤
#     list_filter = ['email','send_type', 'send_time']
# xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)

