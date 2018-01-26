# -*- coding: utf-8 -*-
from django.conf.urls import url

from .applicant import applicant
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^aboutus$',views.about),
    url(r'^applicant$', applicant.applicant),
    url(r'^applicant/applicate$', applicant.applicate),
    url(r'^admin/applicant/list$', applicant.list),#获取HTML页面
    url(r'^admin/applicant/detail', applicant.detail),#返回详细列表
]
