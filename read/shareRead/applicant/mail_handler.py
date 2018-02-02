import smtplib
from email.mime.text import MIMEText
# 审核通过Mail
def adoptMail(applicantEntry):
    host = 'smtp.163.com'
    username = 'gaolong14@163.com'
    password = 'sharereading123'
    to = applicantEntry.mail
    
    subject = "感谢您申请与贫困学子共读活动"
    content = '<span style="font-weight:bold;font-size:18px;">'+applicantEntry.name + '</span> ' + '先生：<br />' if applicantEntry.gender == '男' else '女士：<br />'
    content += '感谢您参加我们的共读活动，与贫困学子共同成长，您的共读小伙伴是：<br />'
    content += '姓名： '+ applicantEntry.selectStudent.lastName + applicantEntry.selectStudent.firstName + '<br />'
    content += '性别： '+ applicantEntry.selectStudent.gender + '<br />'
    content += '生日： '+ applicantEntry.selectStudent.birthday + '<br />'
    content += '年级： '+ applicantEntry.selectStudent.grade + '<br />'
    content += '电话： '+ applicantEntry.selectStudent.tel + '<br />'
    content += '微信： '+ applicantEntry.selectStudent.wechat + '<br />'
    content += '读书兴趣： '+ applicantEntry.selectStudent.interest + '<br />'
    content += '最喜欢的书： '+ applicantEntry.selectStudent.favor + '<br />'
    content += '想读的书： '+ applicantEntry.selectStudent.wish + '<br />'
    content += '提供信息者： '+ applicantEntry.selectStudent.provider + '<br />'
    content += '提供信息者电话： '+ applicantEntry.selectStudent.providerTel + '<br />'
    content += '班主任： '+ applicantEntry.selectStudent.headTeacher + '<br />'
    content += '班主任手机号：'+ applicantEntry.selectStudent.teacherTel + '<br />'
    content += '学校：'+ applicantEntry.selectStudent.school + '<br />'
    content += '备注：'+ applicantEntry.selectStudent.remarks + '<br />'
    content += '请：<br />1、加志愿者微信:1017730430，并注明：孩子编号+您的姓名，我会把你拉入志愿者群。<br />'
    content += '2、加您小伙伴的微信。<br />'
    content += '3、请向孩子家长发送一条短信，可以这样写：您好，我是由【提供信息者】介绍的志愿者xxx，了解到您的一些情况后，'
    content += '想帮助支持您的孩子读书，帮助他更好地成长。我想加您微信，希望您能同意。<br />'
    content += '4、建议您加孩子班主任的微信以便更好的了解情况。<br /><br />'
    content += '再次感谢您的参与！'
        
    
    msg = MIMEText(content.encode('utf8'), _subtype = 'html', _charset = 'utf8')
    msg['Subject'] = u'%s' % subject
    msg['From'] = username
    msg['To'] = to
    
    try:
        server = smtplib.SMTP_SSL(host, 465)
        server.login(username, password)
        server.sendmail(username, to, msg.as_string())
        server.close()
    except Exception as e:
        print('Exception: send email failed:\n')
        print(e)

# 审核拒绝Mail
def rejectMail(applicantEntry):
    host = 'smtp.163.com'
    username = 'gaolong14@163.com'
    password = 'sharereading123'
    to = applicantEntry.mail
    

    subject = "感谢您申请与贫困学子共读活动"
    content = '<span style="font-weight:bold;font-size:18px;">'+applicantEntry.name + '</span> ' + '先生：<br />' if applicantEntry.gender == '男' else '女士：<br />'
    content += '您好，我是共读活动的发起人，感谢您参加我们的共读活动，我们很抱歉地通知您，您的申请未被通过。<br />'
    content += '有疑问可询问：gaolong14@163.com<br />'
    content += '再次感谢您的参与！'
    
    msg = MIMEText(content.encode('utf8'), _subtype = 'html', _charset = 'utf8')
    msg['Subject'] = u'%s' % subject
    msg['From'] = username
    msg['To'] = to
    
    try:
        server = smtplib.SMTP_SSL(host, 465)
        server.login(username, password)
        server.sendmail(username, to, msg.as_string())
        server.close()
    except Exception as e:
        print('Exception: send email failed:\n')
        print(e)