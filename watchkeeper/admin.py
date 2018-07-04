# _*_ coding:utf-8 _*_
from django.contrib import admin
from models import watchkeeper,serverInfo

admin.site.site_header = '盼达值班系统'
admin.site.site_title = '盼达'


@admin.register(watchkeeper)
class opslist(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'qq', 'tag')
    model_name = '值班人员'


@admin.register(serverInfo)
class serverList(admin.ModelAdmin):
    list_display = ('ip','service','cpu','mem','role')