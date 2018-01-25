from django.contrib import admin
from .models import Student
from .models import Applicant
admin.site.register(Student)
admin.site.register(Applicant)
# Register your models here.
admin.site.site_header = "同一本书，同一个梦"
admin.site.site_title='同一本书，同一个梦'