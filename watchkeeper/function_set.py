# _*_ coding:utf-8 _*_
from django.shortcuts import render
#from models import watchkeeper,watchlist
from django.http import HttpResponse
import calendar
import os
import zipfile
import sys

reload(sys)
sys.setdefaultencoding("utf-8")


#  将生成的形如[(name1,phone1),...]的用户电话列表转换成['name1:phone1',...]的列表
def get_name_phone(name_phone_list):
    name_phone_result = []
    for i in range(len(name_phone_list)):
        name_phone_link = name_phone_list[i][0] + ':' + name_phone_list[i][1]
        name_phone_result.append(name_phone_link)
    return name_phone_result


#  此函数用于压缩一个目录中的所有文件
#  传入需要下载的文件路径，压缩后路径，以及压缩后文件名
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


#  判断目录是否存在，不存在则创建
def mkdir(path):
    if os.path.exists(path):
        return u'目录存在'
    else:
        os.makedirs(path)





