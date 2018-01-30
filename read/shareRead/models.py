from django.db import models
from django.forms import ModelForm
import uuid
class Admin(models.Model):
    id = models.IntegerField(primary_key = True)
    userName = models.CharField(max_length=16,verbose_name='用户名')
    password = models.CharField(max_length=16)
    def __str__(self):
        return self.userName
class Student(models.Model):
    TITLE_CHOICES = (
        (0, '待选择'),
        (1, '已经选择'),
        (2, '选择成功'),
    )
    id = models.UUIDField(editable=False,primary_key = True,max_length=32,verbose_name='学生编号',default=uuid.uuid1)
    number = models.UUIDField(max_length=32,verbose_name='编号',default=uuid.uuid1)
    lastName = models.CharField(max_length=16,verbose_name='姓')
    firstName = models.CharField(max_length=16,verbose_name='名')
    gender = models.CharField(max_length=4,verbose_name='性别')
    birthday = models.CharField(max_length=16,verbose_name='生日')
    grade = models.CharField(max_length=8,verbose_name='年级')
    tel = models.CharField(max_length=16,verbose_name='电话号码')
    wechat = models.CharField(max_length=16,verbose_name='家长微信号')
    headTeacher = models.CharField(max_length=32,verbose_name='老师姓名')
    teacherTel = models.CharField(max_length=16,verbose_name='老师手机号')
    teacherWechat=models.CharField(max_length=16,verbose_name='老师微信号')
    like=models.CharField(max_length=255,verbose_name='爱好')
    goodSubjects=models.CharField(max_length=255,verbose_name='擅长科目')
    potentialSubjects=models.CharField(max_length=255,verbose_name='潜力科目')
    interest = models.CharField(max_length=64,verbose_name='读书兴趣')
    favor = models.CharField(max_length=64,verbose_name='喜欢的书')
    wish = models.CharField(max_length=64,verbose_name='想读的书')
    school = models.CharField(max_length=64,verbose_name='所在学校')
    schoolCity=models.CharField(max_length=64,verbose_name='学校所在城市')
    provider = models.CharField(max_length=32,verbose_name='提供信息的公益组织')
    providerTel = models.CharField(max_length=16,verbose_name='联系方式')
    remarks = models.CharField(max_length=256, blank=True,verbose_name='备注')
    status = models.IntegerField(default=0,verbose_name='选择状态',choices=TITLE_CHOICES)
    dateUpdate=models.DateField(auto_now=True)
    dateCreated=models.DateField(auto_now_add=True,blank=True,null=True)
    deleteFlag = models.CharField(max_length=5, default=False,verbose_name="是否删除")
    def __str__(self):
        return self.lastName+self.firstName
    class Meta:
        verbose_name = '学生信息'
        verbose_name_plural = '学生详细填写'
        get_latest_by = "dateUpdate"
        ordering = ['-dateUpdate']
class Applicant(models.Model):
    TITLE_CHOICES = (
        (0, '待审核'),
        (1, '审核通过'),
        (2, '审核拒绝'),
    )
    id = models.UUIDField(editable=False,primary_key = True,db_column='id',default=uuid.uuid1,verbose_name="用户id")
    name = models.CharField(max_length=32,verbose_name='姓名')
    age = models.IntegerField(verbose_name='年龄')
    gender = models.CharField(max_length=4,verbose_name='性别')
    tel = models.CharField(max_length=16,verbose_name='电话')
    wechat = models.CharField(max_length=16,verbose_name='微信')
    mail = models.CharField(max_length=32,verbose_name='邮箱')
    qulification = models.CharField(max_length=16,verbose_name='学历')
    work = models.CharField(max_length=64,verbose_name='工作')
    experience = models.CharField(max_length=512, blank=True,verbose_name='经历')
    goal = models.CharField(max_length=512, blank=True,verbose_name='目标')
    reason = models.CharField(max_length=512, blank=True,verbose_name='原因')
    attitude = models.CharField(max_length=512, blank=True,verbose_name='态度')
    rate = models.CharField(max_length=512, blank=True,verbose_name='频率')
    suitable = models.CharField(max_length=512, blank=True,verbose_name='类型')
    otherTopic = models.CharField(max_length=512, blank=True,verbose_name='其他')
    communicationType = models.CharField(max_length=512, blank=True,verbose_name='交流方式')
    advice = models.CharField(max_length=512, blank=True,verbose_name='建议')
    selectStudent = models.ForeignKey(Student,on_delete=models.DO_NOTHING,verbose_name="选择学生")
    status = models.IntegerField(default=0,verbose_name='审核状态',choices=TITLE_CHOICES)
    dateUpdate = models.DateField(auto_now=True)
    dateCreated = models.DateField(auto_now_add=True, null=True)
    deleteFlag=models.CharField(max_length=5,default=False,verbose_name="是否删除")
    # 0=待审、1=审核通过、2=审核拒绝
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '申请者信息'
        verbose_name_plural = '申请者详细信息'
        get_latest_by = "dateUpdate"
        ordering = ['-dateUpdate']
class StudentForm(ModelForm):
    class Meta:
        model = Student
        exclude = ['id', 'status','deleteFlag']

class ApplicantForm(ModelForm):
    class Meta:
        model = Applicant
        exclude = ['id','status','deleteFlag']
