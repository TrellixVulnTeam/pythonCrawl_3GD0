from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.


class UserAdmin(AbstractUser):
    url = models.TextField('url', max_length=512, blank=True, null=True)
    display_password = models.CharField('铭文密码', max_length=255, blank=True, default='0')
    ymt_name = models.CharField('用户名称', max_length=50, blank=True, null=True)
    ymt_pwd = models.CharField(max_length=64, blank=True, null=True)
    login_ip = models.CharField('IP', max_length=20, blank=True, null=True)
    last_login_time = models.CharField('登入时间', max_length=64, blank=True, null=True)
    is_status = models.CharField('启用状态', max_length=20, blank=True, null=True, default='1')
    is_joke = models.CharField(max_length=20, blank=True, null=True, default='1')
    reqmid = models.CharField(max_length=20, blank=True, null=True)
    channel_type = models.CharField('渠道类型', max_length=20, blank=True, null=True)
    belong = models.CharField('归属', max_length=255, blank=True, null=True, default='')
    cookie = models.TextField('COOKIE', max_length=255, blank=True, null=True, default='')

    class Meta:
        verbose_name = "用户映射"
        verbose_name_plural = verbose_name


class UserBelong(models.Model):
    belong = models.CharField('归属', max_length=255, blank=True, null=True, default='')
    cookie = models.TextField('COOKIE', max_length=255, blank=True, null=True, default='')
    connect_status = models.CharField('连接状态', max_length=255, blank=True, null=True)
    user = models.ForeignKey(UserAdmin, related_name='userbelong', on_delete=models.CASCADE, verbose_name="用户详情",
                             default='')
