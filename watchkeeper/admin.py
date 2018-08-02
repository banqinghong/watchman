# _*_ coding:utf-8 _*_
from django.contrib import admin
import os
from watchman import settings
from models import watchkeeper, serverInfo, ServiceInfo, RunEnv, GroupManage, ConfigManage
from function_set import mkdir


admin.site.site_header = '盼达运维系统'
admin.site.site_title = '盼达'
admin.site.site_url = '/checklist'


@admin.register(watchkeeper)
class OpsList(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'qq', 'group', 'tag', 'comment')
    model_name = '值班人员'
    list_filter = ('group', 'tag')


@admin.register(RunEnv)
class EnvList(admin.ModelAdmin):
    list_display = ('env_name', 'get_role_num', 'comment')

    def get_role_num(self, id):
        num = serverInfo.objects.filter(role_id=id)
        return len(num)

    get_role_num.short_description = '服务器数量'


@admin.register(GroupManage)
class GroupList(admin.ModelAdmin):
    list_display = ('group_name', 'comment')


@admin.register(serverInfo)
class serverList(admin.ModelAdmin):
    list_display = ('nickname', 'ip', 'innerip', 'get_service', 'cpu', 'mem', 'system', 'role', 'comment')
    # fields = ('ip', 'innerip', 'service')
    filter_horizontal = ('service',)
    #raw_id_fields = ('role',)
    list_filter = ('role', )
    search_fields = ('ip', 'nickname', 'service__name')
    list_per_page = 15


@admin.register(ServiceInfo)
class ServiceList(admin.ModelAdmin):
    list_display = ('name', 'nickname', 'packgeName', 'comment')
    list_per_page = 15
    search_fields = ('name', 'nickname')


@admin.register(ConfigManage)
class ConfigList(admin.ModelAdmin):
    list_display = ('filename', 'app_name', 'content_len', 'config_env', 'pub_date', 'update_time')
    list_per_page = 20
    search_fields = ('filename', 'content', 'app_name__name')
    list_filter = ('config_env',)

    #  如果修改了数据，那么将之前的文件删除
    def save_model(self, request, obj, form, change):
        if change:
            role = RunEnv.objects.get(id=obj.config_env_id).env_name
            service = ServiceInfo.objects.get(id=obj.app_name_id).name
            # content = self.model.objects.get(pk=obj.pk).content
            filename = self.model.objects.get(pk=obj.pk).filename
            config_path_dir = os.path.join(settings.MEDIA_ROOT, role, service)
            mkdir(config_path_dir)
            config_path_file = os.path.join(settings.MEDIA_ROOT, role, service, filename)
            if os.path.exists(config_path_file):
                os.remove(config_path_file)

        super(ConfigList, self).save_model(request, obj, form, change)

    # 如果删除一条数据，那么将该数据对应的文件删除
    def delete_model(self, request, obj):
        role = RunEnv.objects.get(id=obj.config_env_id).env_name
        service = ServiceInfo.objects.get(id=obj.app_name_id).name
        # content = self.model.objects.get(pk=obj.pk).content
        filename = self.model.objects.get(pk=obj.pk).filename
        # config_path_dir = os.path.join(settings.MEDIA_ROOT, role, service)
        config_path_file = os.path.join(settings.MEDIA_ROOT, role, service, filename)
        if os.path.exists(config_path_file):
            os.remove(config_path_file)

        super(ConfigList, self).delete_model(request, obj)
