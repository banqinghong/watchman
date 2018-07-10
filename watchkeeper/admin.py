# _*_ coding:utf-8 _*_
from django.contrib import admin
from models import watchkeeper, serverInfo, ServiceInfo, RunEnv

admin.site.site_header = '盼达值班系统'
admin.site.site_title = '盼达'


@admin.register(watchkeeper)
class opslist(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'qq', 'tag')
    model_name = '值班人员'


@admin.register(RunEnv)
class envlist(admin.ModelAdmin):
    list_display = ('env_name', 'get_role_num')

    def get_role_num(self, id):
        num = serverInfo.objects.filter(role_id=id)
        return len(num)

    get_role_num.short_description = '服务器数量'


@admin.register(serverInfo)
class serverList(admin.ModelAdmin):
    list_display = ('nickname', 'ip', 'innerip', 'get_service', 'cpu', 'mem', 'role')
    # fields = ('ip', 'innerip', 'service')
    filter_horizontal = ('service',)
    raw_id_fields = ('role',)
    list_filter = ('role', 'cpu', 'mem')
    search_fields = ('ip', 'nickname', 'service__name')


@admin.register(ServiceInfo)
class ServiceList(admin.ModelAdmin):
    list_display = ('name', 'packgeName')
