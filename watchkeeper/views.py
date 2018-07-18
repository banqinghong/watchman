# _*_ coding:utf-8 _*_
from django.shortcuts import render
from models import watchkeeper, watchlist
from django.http import HttpResponse
import calendar
from django.contrib.auth.decorators import login_required


# Create your views here.

def acc_login(request):
    return render(request, 'login.html')


@login_required
def addPage(request):
    namelist = watchkeeper.objects.filter(group_id=1, tag=0).values_list('name', 'phone').order_by('id')
    namelist_lvzhou = watchkeeper.objects.filter(group_id=2, tag=0).values_list('name', 'phone').order_by('id')
    namedict_lv = dict(namelist_lvzhou)
    namedict = dict(namelist)
    return render(request, 'addpage.html', {'namelist': namedict, 'namelist_lvzhou': namedict_lv})


@login_required
def addwatchman(request):
    name = request.POST.get('name')
    phonenum = request.POST.get('phone')
    watchkeeper.objects.update_or_create(name=name, phone=phonenum, tag=0)
    return render(request, 'ksuccess.html', {'name': name, 'phone': phonenum})


@login_required
def listwatchman(request):
    year = request.POST.get('year')
    month = request.POST.get('month')
    watch_list = watchlist.objects.filter(month=month, year=year).values_list('name', flat=True).order_by('id')
    namelist_lvzhou = watchkeeper.objects.filter(group_id=2, tag=0).values_list('name', 'phone').order_by('id')
    namelist = watchkeeper.objects.filter(group_id=1, tag=0).values_list('name', 'phone').order_by('id')
    namedict = dict(namelist)
    namedict_lv = dict(namelist_lvzhou)
    return render(request, 'listpage.html', {'nameList': watch_list, 'namelist': namedict,  'namelist_lvzhou': namedict_lv, 'year': year, 'month': month})


@login_required
def checklist(request):
    namelist = watchkeeper.objects.filter(group_id=1, tag=0).values_list('name', 'phone').order_by('id')
    namelist_lvzhou = watchkeeper.objects.filter(group_id=2, tag=0).values_list('name', 'phone').order_by('id')
    namedict_lv = dict(namelist_lvzhou)
    namedict = dict(namelist)

    return render(request, 'check.html', {'namelist': namedict, 'namelist_lvzhou': namedict_lv})


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
