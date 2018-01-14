# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views
from .student import student
from .student import applicant
urlpatterns = [
    url(r'^$', views.index),
    url(r'^aboutus$',views.about),
    url(r'^applicant$', applicant.applicant),
    url(r'^applicant/applicate$', applicant.applicate),
]
