# -*- coding: utf-8 -*-
from django.conf.urls import url

from .applicant import applicant
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^aboutus$', views.about),
    url(r'^applicant$', applicant.applicant),
    url(r'^applicant/applicate$', applicant.applicate),
    url(r'^admin/applicant/list$', applicant.list),  # 获取HTML页面
    url(r'^admin/applicant/detail', applicant.detail),  # 返回详细列表
    url(r'^admin/applicant/adopt$', applicant.adopt),  # 审核成功
    url(r'^admin/applicant/reject$', applicant.reject),  # 审核拒绝
    url(r'^admin/applicant/delete', applicant.deleteApplicant),  # 删除用户
]
handler404 = views.error
