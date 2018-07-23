# _*_ coding:utf-8 _*_
from django.db import models
import sys

reload(sys)
sys.setdefaultencoding("utf-8")

# Create your models here.
class GroupManage(models.Model):
    group_name = models.CharField(default="", blank=True, verbose_name='组名', max_length=30)
    comment = models.TextField(default="", blank=True, verbose_name='备注')

    def __unicode__(self):
        return self.group_name

    class Meta:
        verbose_name = '组织管理'
        verbose_name_plural = '组织管理'


class watchkeeper(models.Model):
    tag_default = 0
    tag_need_not = 1
    tag_choice = (
        (tag_default, '需要'),
        (tag_need_not, '不需要')
    )
    name = models.CharField(default="", blank=True, verbose_name='姓名', max_length=30)
    phone = models.CharField(verbose_name='电话', blank=True, max_length=11, default="")
    qq = models.CharField(verbose_name='QQ号', blank=True, max_length=13, default="")
    email = models.EmailField(verbose_name='邮箱', blank=True, default="")
    group = models.ForeignKey(GroupManage, default="", blank=True, verbose_name=u'所属组织', max_length=20)
    tag = models.IntegerField(default=tag_default, choices=tag_choice, verbose_name='是否需要值班')
    comment = models.TextField(default="", blank=True, verbose_name='备注')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = '人员管理'
        verbose_name_plural = '人员管理'


class ServiceInfo(models.Model):
    name = models.CharField(default="", blank=True, verbose_name='服务名称', max_length=30)
    nickname = models.CharField(default="", blank=True, verbose_name='服务简写', max_length=30)
    packgeName = models.CharField(default="", blank=True, verbose_name='包名称', max_length=50)
    comment = models.TextField(default="", blank=True, verbose_name='备注')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = '服务管理'
        verbose_name_plural = '服务管理'


class RunEnv(models.Model):
    env_name = models.CharField(default="stage", blank=True, verbose_name='运行环境', max_length=30)
    comment = models.TextField(default="", blank=True, verbose_name='备注')

    def __unicode__(self):
        return self.env_name

    class Meta:
        verbose_name = '环境管理'
        verbose_name_plural = '环境管理'


class watchlist(models.Model):
    name = models.CharField(max_length=30)
    day = models.IntegerField()
    month = models.IntegerField()
    year = models.IntegerField()

    class Meta:
        verbose_name = '值班表'
        verbose_name_plural = '值班表'

    def __unicode__(self):
        return self.name


class serverInfo(models.Model):
    nickname = models.CharField(verbose_name='hostname', max_length=20)
    ip = models.GenericIPAddressField(verbose_name='外网IP')
    innerip = models.GenericIPAddressField(default='', null=True, blank=True, verbose_name='内网IP')
    # service = models.TextField(verbose_name='运行服务')
    service = models.ManyToManyField(ServiceInfo, blank=True, verbose_name=u'运行服务')
    cpu = models.IntegerField(verbose_name='CPU(核)')
    mem = models.IntegerField(verbose_name='内存（G）')
    system = models.CharField(verbose_name='操作系统', null=True, blank=True, max_length=50)
    role = models.ForeignKey(RunEnv, default="", blank=True, verbose_name=u'运行环境', max_length=20)
    comment = models.TextField(default="", blank=True, verbose_name='备注')

    class Meta:
        verbose_name = '主机管理'
        verbose_name_plural = '主机管理'

    def get_service(self):
        return ",".join([p.name for p in self.service.all()])

    get_service.short_description = '运行服务'

    def __unicode__(self):
        return self.ip


class ConfigManage(models.Model):
    filename = models.CharField(default="", blank=True, verbose_name='文件名', max_length=50)
    app_name = models.ForeignKey(ServiceInfo, default="", verbose_name=u'所属服务')
    content = models.TextField(default="", verbose_name='配置内容')
    config_env = models.ForeignKey(RunEnv, default="", verbose_name=u'所属环境')
    pub_date = models.DateTimeField(verbose_name='上传时间', auto_now_add=True)
    update_time = models.DateTimeField(verbose_name='更新时间', auto_now=True, null=True)

    class Meta:
        verbose_name = '配置管理'
        verbose_name_plural = '配置管理'

    def __unicode__(self):
        return self.filename

    def content_len(self):
        if len(str(self.content)) > 40:
            return '{}......'.format(str(self.content)[0:40])
        else:
            return str(self.content)
    content_len.short_description = '配置内容'

