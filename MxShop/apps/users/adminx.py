# users/adminx.py
__author__ = 'derek'

import xadmin
from xadmin import views
from .models import VerifyCode


class BaseSetting(object):
    # 添加主题功能
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    # 全局配置，后台管理标题和页脚
    site_title = "后台 & Dog"
    site_footer = "Powered By a Handsome Man"
    # 菜单收缩
    menu_style = "accordion"


class VerifyCodeAdmin(object):
    list_display = ['code', 'mobile', "add_time"]


xadmin.site.register(VerifyCode, VerifyCodeAdmin)  # models 和 模型中具体哪块 注册到xadmin
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)
