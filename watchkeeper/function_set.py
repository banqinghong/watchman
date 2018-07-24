# _*_ coding:utf-8 _*_
from django.shortcuts import render
from models import watchkeeper, watchlist
from django.http import HttpResponse
import calendar
import os
import zipfile
import sys

reload(sys)
sys.setdefaultencoding("utf-8")


def get_name_phone(name_phone_list):
    name_phone_result = []
    for i in range(len(name_phone_list)):
        name_phone_link = name_phone_list[i][0] + ':' + name_phone_list[i][1]
        name_phone_result.append(name_phone_link)
    return name_phone_result


def zip_file(source_path, output_path, output_name):
    os.chdir(source_path)
    workdir = '.'
    file_list = os.listdir(workdir)
    sys_sep = os.path.sep
    output_file = output_path + sys_sep + output_name + '.zip'
    with zipfile.ZipFile(output_file, 'w') as z:
        for filename in file_list:
            file_path = os.path.join(workdir, filename)
            z.write(file_path)
        z.close()
    return output_file






