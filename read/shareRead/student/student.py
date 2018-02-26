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
        jsonData={"姓名":studentEntry.lastName+studentEntry.lastName,
                  "生日":studentEntry.birthday,
                  "年级":studentEntry.grade,
                  "爱好":studentEntry.like,
                  "擅长科目":studentEntry.goodSubjects,
                  "潜力科目":studentEntry.potentialSubjects,
                  "读书兴趣":studentEntry.interest,
                  "喜欢的书":studentEntry.favor,
                  "想读的书": studentEntry.wish,
                  "所在学校":studentEntry.school,
                  "学校所在城市":studentEntry.schoolCity,
                  "备注":studentEntry.remarks
                  }
        return HttpResponse(json.dumps(jsonData), content_type="application/json")
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