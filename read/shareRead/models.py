from django.db import models
from django.forms import ModelForm

class Admin(models.Model):
    id = models.IntegerField(primary_key = True)
    userName = models.CharField(max_length=16)
    password = models.CharField(max_length=16)

class Student(models.Model):
    id = models.IntegerField(primary_key = True)
    number = models.CharField(max_length=8)
    lastName = models.CharField(max_length=16)
    firstName = models.CharField(max_length=16)
    gender = models.CharField(max_length=4)
    birthday = models.CharField(max_length=16)
    grade = models.CharField(max_length=8)
    tel = models.CharField(max_length=16)
    wechat = models.CharField(max_length=16)#家长微信号
    headTeacher = models.CharField(max_length=32)#老师姓名
    teacherTel = models.CharField(max_length=16)#老师手机号
    teacherWechat=models.CharField(max_length=16)#老师微信号
    like=models.CharField(max_length=255)#爱好
    goodSubjects=models.CharField(max_length=255)#擅长科目
    potentialSubjects=models.CharField(max_length=255)#潜力科目
    interest = models.CharField(max_length=64)#读书兴趣
    favor = models.CharField(max_length=64)#喜欢的书
    wish = models.CharField(max_length=64)#想读的书
    school = models.CharField(max_length=64)#所在学校
    schoolCity=models.CharField(max_length=64)#学校所在城市
    provider = models.CharField(max_length=32)#提供信息的公益组织
    providerTel = models.CharField(max_length=16)#联系方式
    remarks = models.CharField(max_length=256, blank=True)#备注
    status = models.IntegerField(default=0) # 0=未选择、1=待审核、2=已选择
class Applicant(models.Model):
    id = models.IntegerField(primary_key = True,db_column='id',default=1)
    name = models.CharField(max_length=32)
    age = models.IntegerField()
    gender = models.CharField(max_length=4)
    tel = models.CharField(max_length=16)
    wechat = models.CharField(max_length=16)
    mail = models.CharField(max_length=32)
    qulification = models.CharField(max_length=16)
    work = models.CharField(max_length=64)
    experience = models.CharField(max_length=512, blank=True)
    goal = models.CharField(max_length=512, blank=True)
    reason = models.CharField(max_length=512, blank=True)
    attitude = models.CharField(max_length=512, blank=True)
    rate = models.CharField(max_length=512, blank=True)
    suitable = models.CharField(max_length=512, blank=True)
    otherTopic = models.CharField(max_length=512, blank=True)
    communicationType = models.CharField(max_length=512, blank=True)
    advice = models.CharField(max_length=512, blank=True)
    selectStudent = models.ForeignKey(Student,on_delete=models.DO_NOTHING)
    status = models.IntegerField(default=0) # 0=待审、1=审核通过、2=审核拒绝


class StudentForm(ModelForm):
    class Meta:
        model = Student
        exclude = ['id', 'status']

class ApplicantForm(ModelForm):
    class Meta:
        model = Applicant
        exclude = ['id','status']
