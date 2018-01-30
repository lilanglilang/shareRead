# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from ..models import ApplicantForm
from ..models import Student
from ..models import Applicant
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.core import serializers
import json
def applicant(request):
    studentId = request.GET['studentId']
    studentEntry = Student.objects.get(id=studentId)
    return render(request,'shareRead/applicate.html', {'studentEntry': studentEntry})
# 提交申请
@csrf_exempt
def applicate(request):
    applicantForm = ApplicantForm(request.POST)
    idstu=str(applicantForm.data['selectStudent']).replace("-","")
    studentEntry = Student.objects.get(id=idstu)

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
        pass
@login_required(login_url='/admin')
def detail(request):
    try:
        applicantList = Applicant.objects.all()
        json_data=serializers.serialize("json",applicantList)
        data=json.loads(json_data)
        count=len(data)
        Rows=[]
        for x in  data:
            dictdata=x['fields']
            dictdata['id']=x['pk']
            Rows.append(dictdata)
        return HttpResponse(json.dumps({"code":0,"msg":"",'count':count,'data':Rows}), content_type="application/json")
    except:
        pass

