# _*_ coding:utf-8 _*_
from django.shortcuts import render
from models import watchkeeper, watchlist, RunEnv, ServiceInfo
from watchman import settings
from function_set import get_name_phone, zip_file
from django.http import HttpResponse
import calendar
import os
from django.contrib.auth.decorators import login_required
import sys

reload(sys)
sys.setdefaultencoding("utf-8")

# Create your views here.

def acc_login(request):
    return render(request, 'login.html')


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
def bulk_down(request):
    role = request.POST.get('role')
    service = request.POST.get('service')
    tmp_dir = os.path.join(settings.BASE_DIR, 'tmp')
    input_file = os.path.join(settings.MEDIA_ROOT, str(role), str(service))
    output_name = '{0}-{1}'.format(str(role), str(service))
    unicode_input_file = unicode(input_file, "utf-8")
    unicode_tmp_dir = unicode(tmp_dir, "utf-8")
    unicode_output_name = unicode(output_name, "utf-8")
    try:
        os.chdir(input_file)
        zip_file(unicode_input_file, unicode_tmp_dir, unicode_output_name)
        return_name = str(role)+str(service)
    except WindowsError:
        return_name = '{} 环境中不存在 {} 项目'.format(role, service)

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
    return render(request, 'listpage.html', {'nameList': watch_list, 'namelist': name_phone,  'namelist_lvzhou':name_phone_lv, 'year': year, 'month': month})


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


@login_required
def addwatchlist(request):
    month_post = request.POST.get('month')
    year_post = request.POST.get('year')
    month = int(str(month_post))
    year = int(str(year_post))
    num_post = request.POST.get('num')
    num = int(str(num_post))
    num_post_lv  = request.POST.get('num_lv')
    num_lv = int(str(num_post_lv))
    namelist = watchkeeper.objects.values_list('name').filter(group_id=1, tag=0).order_by('id')
    namelist_lvzhou = watchkeeper.objects.filter(group_id=2, tag=0).values_list('name', flat=True).order_by('id')
    monthList = calendar.monthcalendar(year, month)
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
                name_lv = namelist_lvzhou[num_lv-1]
                watchlist.objects.update_or_create(year=year, day=monthList[i][j], month=month, name=name_lv)
                num_lv += 1
            else:
                name_lv = namelist_lvzhou[num_lv-1]
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
