from django.db.models import Count
from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template
from django.views.decorators.csrf import csrf_exempt

from .models import Student
import datetime
# Create your views here.
#定义公用模块的位置
def index(request):
    # 爱心人士获取学生信息列表
    # studentList = Student.objects.filter(status=0).order_by('school')
    meaningTime=datetime.datetime.now().year
    # return render(request,'shareRead/students.html', {'meaningTime':meaningTime,'studentList': studentList, 'size': len(studentList)})
    return render(request,'shareRead/students.html',context={'meaningTime':meaningTime})
def about(request):
    return render(request,'shareRead/aboutus.html')
def error(request):
    return render(request, 'shareRead/error.html')

@csrf_exempt
def regDiv(request):
    if request.is_ajax():
        cityList = Student.objects.values("schoolCity").annotate(cities=Count("schoolCity")).filter(status=0).order_by("schoolCity")
        regList = Student.objects.filter(status=0).order_by('schoolCity')
        # t = get_template('shareRead/regList.html')  # get the contex of html
        # content_html = t.render({'regList': regList,'cityList': cityList})  # render the template to the local html you want,rather than return a variable
        return render(request,template_name='shareRead/regList.html',context={'regList': regList,
                                 'cityList': cityList})
