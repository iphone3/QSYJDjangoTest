from random import Random
from users.models import EmailVerifyRecord
from django.core.mail import send_mail
from QSYJDjangoTest.settings import EMAIL_FROM

# 邮箱验证 [激活、修改密码]
def send_email(email, send_type=0):
    email_record = EmailVerifyRecord()
    email_record.code = generate_random_str(16)
    email_record.email = email
    email_record.send_type = send_type
    email_record.save()

    # 发送邮件
    email_title = ''
    email_body = ''

    if send_type == 0:  # 注册后的激活操作
        email_title = '全视眼镜商城——激活操作'
        email_body = '激活链接: xxxxx/active/{0}'.format(email_record.code)
    elif send_type == 1:    # 修改密码操作
        pass

    # 发送邮箱前，需要配置好发送者
    send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
    if send_status:
        print('发送成功')

# 生成验证码
def generate_random_str(random_len=8):
    str = ''
    chars = 'qwertyuiopasdfghjklzxxcvbnmQWERTYUIOPASDFGHJKLZXXCVBNM'
    length = len(chars) - 1
    random = Random()

    for i in range(random_len):
        str += chars[random.randint(0, length)]

    return str
