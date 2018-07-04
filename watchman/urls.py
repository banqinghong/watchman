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


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^addpage$',myviews.addPage,name='addpage'),
    url(r'^addwatchkeeper/$',myviews.addwatchman,name='addwatchkeeper'),
    url(r'^addwatchlist/$',myviews.addwatchlist,name='addwatchlist'),
    url(r'^listwatch/$',myviews.listwatchman,name='listwatch'),
    url(r'^checklist/$',myviews.checklist,name='listwatch'),
    url(r'^deletelist/$',myviews.deletelist,name='listwatch'),
    url(r'^delwatchkeeper/$',myviews.delwatchman,name='delwatchkeeper'),
    url(r'^$',myviews.checklist,name='index'),
]
