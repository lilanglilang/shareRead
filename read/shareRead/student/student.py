# -*- coding: utf-8 -*-
from ..models import Student
from ..models import Applicant
from django.http import HttpResponse
from django.shortcuts import render
import json
def getStudentInfo(request):
    applicantId = request.GET['applicantId']
    if applicantId is None:
        return render("shareRead/error.html")
    try:
        # 修改申请者状态
        applicantId = applicantId.replace("-", "")
        applicantEntry = Applicant.objects.get(id=applicantId)
        studentEntry=applicantEntry.selectStudent
        return HttpResponse(json.dumps({"姓名":studentEntry.lastName+studentEntry.lastName,"爱好":studentEntry.like}), content_type="application/json")
    except BaseException as e:
        # 修改申请者状态
        applicantEntry = Applicant.objects.get(id=applicantId)
        applicantEntry.status = 0
        applicantEntry.save()

        # 修改学生状态
        studentEntry = Student.objects.get(id=applicantEntry.selectStudent.id)
        studentEntry.status = 1
        studentEntry.save()
        return HttpResponse(json.dumps({"messsage": "审核失败"}), content_type="application/json")