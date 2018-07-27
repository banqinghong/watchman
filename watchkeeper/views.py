# _*_ coding:utf-8 _*_
from django.shortcuts import render
from models import watchkeeper, watchlist, RunEnv, ServiceInfo, ConfigManage
from watchman import settings
from function_set import get_name_phone, zip_file
from django.http import HttpResponse, StreamingHttpResponse
import calendar
import os
from django.contrib.auth.decorators import login_required
import sys

reload(sys)
sys.setdefaultencoding("utf-8")


# Create your views here.

def acc_login(request):
    return render(request, 'login.html')


def mkdir(path):
    if os.path.exists(path):
        return u'目录存在'
    else:
        os.mkdir(path)


@login_required
def addPage(request):
    namelist = watchkeeper.objects.filter(group_id=1, tag=0).values_list('name', 'phone').order_by('id')
    namelist_lvzhou = watchkeeper.objects.filter(group_id=2, tag=0).values_list('name', 'phone').order_by('id')
    name_phone = get_name_phone(namelist)
    name_phone_lv = get_name_phone(namelist_lvzhou)
    return render(request, 'addpage.html', {'namelist': name_phone, 'namelist_lvzhou': name_phone_lv})


@login_required
def addwatchman(request):
    name = request.POST.get('name')
    phonenum = request.POST.get('phone')
    watchkeeper.objects.update_or_create(name=name, phone=phonenum, tag=0)
    return render(request, 'ksuccess.html', {'name': name, 'phone': phonenum})


@login_required
def bulk_down_page(request):
    role_list = RunEnv.objects.values_list('env_name', flat=True)
    service_list = ServiceInfo.objects.values_list('name', flat=True)
    return render(request, 'bulk_down.html', {'role_list': role_list, 'service_list': service_list})


@login_required
def config_upload(request):
    role = request.POST.get('role')
    role_id = RunEnv.objects.filter(env_name=role).values_list('id', flat=True)[0]
    service = request.POST.get('service')
    service_id = ServiceInfo.objects.filter(name=service).values_list('id', flat=True)[0]
    my_files = request.FILES.get('my_file', None)
    if not my_files:
        return HttpResponse(u'未上传任何文件')
    config_path_dir = os.path.join(settings.MEDIA_ROOT, role, service)
    config_path_store = os.path.join(settings.MEDIA_ROOT, role, service, my_files.name)
    if os.path.exists(config_path_store):
        os.remove(config_path_store)
    if not os.path.exists(config_path_dir):
        os.makedirs(config_path_dir)
    file_write = open(config_path_store, 'wb+')
    for chunk in my_files.chunks():
        file_write.write(chunk)
    file_write.close()
    file_read = open(config_path_store, 'r')
    content = file_read.read()
    config_filter = ConfigManage.objects.filter(filename=my_files.name, app_name_id=service_id, config_env_id=role_id)
    if config_filter:
        config_filter.update(content=content)
    else:
        ConfigManage.objects.create(filename=my_files.name, app_name_id=service_id, config_env_id=role_id, content=content)
    return render(request, 'update_success.html')


@login_required
def bulk_down(request):
    role = request.POST.get('role')
    service = request.POST.get('service')
    tmp_dir = settings.TMP_DIR
    mkdir(tmp_dir)
    sys_sep = os.path.sep
    input_file = os.path.join(settings.MEDIA_ROOT, str(role), str(service))
    output_name = '{0}-{1}'.format(str(role), str(service))
    unicode_input_file = unicode(input_file, "utf-8")
    unicode_tmp_dir = unicode(tmp_dir, "utf-8")
    unicode_output_name = unicode(output_name, "utf-8")
    try:
        os.listdir(unicode_input_file)
        zip_file(unicode_input_file, unicode_tmp_dir, unicode_output_name)
        down_file = unicode_tmp_dir + sys_sep + unicode_output_name + '.zip'
        file = open(down_file, 'rb')
        response = StreamingHttpResponse(file, content_type='application/zip')
        response['Content-Disposition'] = 'attachment;filename="{0}.zip"'.format(output_name)
        return response
    except WindowsError:
        return_name = '{}环境没有 {}项目'.format(role, service)
        return HttpResponse(return_name)


@login_required
def listwatchman(request):
    year = request.POST.get('year')
    month = request.POST.get('month')
    watch_list = watchlist.objects.filter(month=month, year=year).values_list('name', flat=True).order_by('id')
    namelist_lvzhou = watchkeeper.objects.filter(group_id=2, tag=0).values_list('name', 'phone').order_by('id')
    namelist = watchkeeper.objects.filter(group_id=1, tag=0).values_list('name', 'phone').order_by('id')
    name_phone = get_name_phone(namelist)
    name_phone_lv = get_name_phone(namelist_lvzhou)
    return render(request, 'listpage.html',
                  {'nameList': watch_list, 'namelist': name_phone, 'namelist_lvzhou': name_phone_lv, 'year': year,
                   'month': month})


@login_required
def checklist(request):
    namelist = watchkeeper.objects.filter(group_id=1, tag=0).values_list('name', 'phone').order_by('id')
    namelist_lvzhou = watchkeeper.objects.filter(group_id=2, tag=0).values_list('name', 'phone').order_by('id')
    name_phone = get_name_phone(namelist)
    name_phone_lv = get_name_phone(namelist_lvzhou)

    return render(request, 'check.html', {'namelist': name_phone, 'namelist_lvzhou': name_phone_lv})


@login_required
def deletelist(request):
    year = request.POST.get('year')
    month = request.POST.get('month')
    watchlist.objects.filter(month=month, year=year).delete()
    return HttpResponse(u"删除成功")


@login_required
def delwatchman(request):
    name = request.POST.get('name')
    watchkeeper.objects.filter(name=name).delete()
    return HttpResponse(u"删除成功")


#  根据用户输入的年月，起始值班人员等信息，生成值班信息并写入数据库
@login_required
def addwatchlist(request):
    month_post = request.POST.get('month')
    year_post = request.POST.get('year')
    #  转换格式
    month = int(str(month_post))
    year = int(str(year_post))
    #  根据用户输入的顺序获取起始值班人员名字
    num_post = request.POST.get('num')
    num = int(str(num_post))
    num_post_lv = request.POST.get('num_lv')
    num_lv = int(str(num_post_lv))
    #  获取需要值班人员的名字列表  _lv _lvzhou 表示绿洲值班人员（按周轮班）
    namelist = watchkeeper.objects.values_list('name').filter(group_id=1, tag=0).order_by('id')
    namelist_lvzhou = watchkeeper.objects.filter(group_id=2, tag=0).values_list('name', flat=True).order_by('id')
    monthList = calendar.monthcalendar(year, month)  # 获取当月日期表
    # namelist_list列表为当前值班表中的数据，如果有则返回已经存在，如果没有则生成
    namelist_list = watchlist.objects.filter(month=month, year=year).values_list('name', flat=True).order_by('id')
    if len(namelist_list) == 0:
        for i in range(len(monthList)):
            for j in range(7):
                if monthList[i][j] == 0:
                    watchlist.objects.create(year=year, day=monthList[i][j], month=month, name='space')
                else:
                    if num < len(namelist):
                        name = namelist[num - 1][0]
                        new = "%s--->%s" % (monthList[i][j], name)
                        watchlist.objects.update_or_create(year=year, day=monthList[i][j], month=month, name=new)
                        num += 1
                    else:
                        name = namelist[num - 1][0]
                        new = "%s--->%s" % (monthList[i][j], name)
                        watchlist.objects.update_or_create(year=year, day=monthList[i][j], month=month, name=new)
                        num = 1
            if num_lv < len(namelist_lvzhou):
                name_lv = namelist_lvzhou[num_lv - 1]
                watchlist.objects.update_or_create(year=year, day=monthList[i][j], month=month, name=name_lv)
                num_lv += 1
            else:
                name_lv = namelist_lvzhou[num_lv - 1]
                watchlist.objects.update_or_create(year=year, day=monthList[i][j], month=month, name=name_lv)
                num_lv = 1
            watchlist.objects.create(year=year, day=monthList[i][j], month=month, name='enter')
        namelist_success = watchlist.objects.filter(month=month, year=year).values_list('name', flat=True).order_by(
            'id')
        return render(request, 'lsuccess.html', {'year': year, 'month': month, 'nameList': namelist_success})
    else:
        result = u"值班表已存在，如下："
        return render(request, 'listpage.html',
                      {'nameList': namelist_list, 'year': year, 'month': month, 'result': result})
