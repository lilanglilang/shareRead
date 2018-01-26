# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from ..models import ApplicantForm
from ..models import Student
from ..models import Applicant
from django.contrib.auth.decorators import login_required
def applicant(request):
    studentId = request.GET['studentId']
    studentEntry = Student.objects.get(id=studentId)
    return render(request,'shareRead/applicate.html', {'studentEntry': studentEntry})
# 提交申请
@csrf_exempt
def applicate(request):
    applicantForm = ApplicantForm(request.POST)
    studentEntry = Student.objects.get(id=applicantForm.data['selectStudent'])

    # 字段验证
    if applicantForm.is_valid():
        # 修改学生状态为待审核
        if studentEntry.status == 0:
            studentEntry.status = 1
            studentEntry.save()
        else:
            return render(request,'shareRead/applicate.html', {'hint': '对不起，已经有其他热心朋友选定了该小朋友，请您选择其他愿意帮助的小朋友。','studentEntry': studentEntry})

        applicantForm.save()
    else:
        return render(request,'shareRead/applicate.html',  {'hint': '字段错误！',
             'studentEntry': studentEntry})

    return render(request,'shareRead/applicate_success.html')

@login_required(login_url='/admin')
def list(request):
    try:
        applicantList = Applicant.objects.all()
        return render(request, 'shareRead/applicant_list.html',{'applicant': applicantList})
    except:
        request
