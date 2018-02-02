from django.shortcuts import render
from .models import Student
# Create your views here.
#定义公用模块的位置
def index(request):
    # 爱心人士获取学生信息列表
    studentList = Student.objects.filter(status=0)
    return render(request,'shareRead/students.html', {'studentList': studentList, 'size': len(studentList)})
def about(request):
    return render(request,'shareRead/aboutus.html')
def error(request):
    return render(request, 'shareRead/error.html')