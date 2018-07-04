# _*_ coding:utf-8 _*_
from django.apps import AppConfig


default_app_config = 'watchkeeper.KeeperManage'


class KeeperManage(AppConfig):
    name = 'watchkeeper'
    verbose_name = u"运维管理"
