import hashlib
import time
import uuid
from random import Random
from django.core.mail import EmailMessage
from django.template import loader

from QSYJDjangoTest.settings import EMAIL_FROM, ACTIVE_LINK
from django.core.cache import cache


# 邮箱验证 [激活、修改密码]
def send_email(username ,email, send_type=0):
    # 使用缓存的方式，以便于超时处理 [也可以配置上redis或直接django底层缓存api]
    # set(key, value, timeout)  >> set(code, email, timeout)


    # 发送邮件
    email_title = ''
    email_body = ''
    code = ''
    timeout = 0

    if send_type == 0:  # 注册后的激活操作
        code = generate_active_code()
        timeout = 60 * 1   # 激活操作，半小时生效
        email_title = '全视眼镜商城——激活操作'
        active_url = '{0}/active/{1}'.format(ACTIVE_LINK,code)
        email_body = loader.render_to_string('active_email.html', {'username':username, 'active_url':active_url})
    elif send_type == 1:    # 修改密码操作
        pass

    # 发送邮箱前，需要配置好发送者
    msg = EmailMessage(email_title, email_body, EMAIL_FROM, [email])
    msg.content_subtype = "html"    # 发送邮件中主体内容可以是HTML/TEXT
    send_status = msg.send()
    if send_status:
        # 发送成功，进行缓存，计时
        cache.set(code, email, timeout=timeout)
        print('发送成功')


# 生成激活码
def generate_active_code():
    hash = hashlib.sha512()
    sha_str = str(uuid.uuid4()) + str(int(time.time()))
    hash.update(sha_str.encode('utf-8'))

    return hash.hexdigest()

# 生成验证码[修改密码]
def generate_random_str(random_len=4):
    str = ''
    chars = 'qwertyuiopasdfghjklzxxcvbnmQWERTYUIOPASDFGHJKLZXXCVBNM'
    length = len(chars) - 1
    random = Random()

    for i in range(random_len):
        str += chars[random.randint(0, length)]

    return str
