# -*- coding: utf-8 -*-
from django.conf.urls import url

from .applicant import applicant
from  .student import student
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^aboutus$', views.about),
    # edited by skaudrey
    url(r'^regDiv$', views.regDiv) , # return the studentlist grouped by city
    url(r'^applicant$', applicant.applicant),
    url(r'^applicant/applicate$', applicant.applicate),
    url(r'^admin/applicant/list$', applicant.list),  # 返回详细列表
    url(r'^admin/applicant/detail', applicant.detail),
    url(r'^admin/applicant/adopt$', applicant.adopt),  # 审核成功
    url(r'^admin/applicant/reject$', applicant.reject),  # 审核拒绝
    url(r'^admin/applicant/delete', applicant.deleteApplicant),  # 删除用户
    url(r'^admin/student/studentInfo', student.getStudentInfo),  # 删除用户
]
handler404 = views.error
