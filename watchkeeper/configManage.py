# _*_ coding:utf-8 _*_
from django.shortcuts import render
from models import watchkeeper, watchlist
from django.http import HttpResponse
import calendar
from django.contrib.auth.decorators import login_required


@login_required
def my_test(request):
    return HttpResponse(u"删除成功")
