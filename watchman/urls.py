# _*_ coding:utf-8 _*_
"""watchman URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from watchkeeper import views as myviews
from django.views.static import serve
from watchman import settings


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^addpage$', myviews.addPage, name='addpage'),
    url(r'^addwatchkeeper/$', myviews.addwatchman, name='addwatchkeeper'),
    url(r'^addwatchlist/$', myviews.addwatchlist, name='addwatchlist'),
    url(r'^listwatch/$', myviews.listwatchman, name='listwatch'),
    url(r'^checklist/$', myviews.checklist, name='checklist'),
    url(r'^deletelist/$', myviews.deletelist, name='deletelist'),
    url(r'^delwatchkeeper/$', myviews.delwatchman, name='delwatchkeeper'),
    url(r'^down_page/$', myviews.bulk_down_page, name='down_page'),
    url(r'^bulk_down$', myviews.bulk_down, name='bulk_down'),
    url(r'^$', myviews.checklist, name='index'),
    url(r'^config/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
]
