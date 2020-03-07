"""
Django settings for QSYJDjangoTest project.

Generated by 'django-admin startproject' using Django 1.11.13.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
import sys

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 添加apps后，要加入到Python的搜索目录下
sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))
sys.path.insert(0,os.path.join(BASE_DIR, 'extra_apps'))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'r$(pu24ha3l=ly4^7l$u%u)vc^txevtttv!nbc0$nbb)&m521y'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'users',
    'goods',
    'operation',
    'xadmin',   # xadmin
    'crispy_forms', # xadmin
    'captcha',  # 验证码
    'pure_pagination',  # 分页器
]


# 重载该profile才能生效  [应用名+类名]
AUTH_USER_MODEL = 'users.UserProfile'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'QSYJDjangoTest.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates')
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                # MEDIA_URL配置
                # 配置好之后，就会将MEDIA_URL注册到HTML中，即HTML就可以使用MEDIA_URL变量
                'django.template.context_processors.media'
            ],
            'libraries': {  # 自定义过滤器注册
                'get_item': 'apps.utils.get_item',
            },
        },
    },
]

WSGI_APPLICATION = 'QSYJDjangoTest.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'qsyjTest',
        'USER': 'root',
        'PASSWORD': '123456',
        'HOST': '127.0.0.1',
        'POST': '3306'
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'zh-Hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

# True时Django，会设置为国际时间
# False为本地时间
USE_TZ = False


# 静态文件
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

# 上传文件
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# 自定义认证处理
AUTHENTICATION_BACKENDS = (
    'users.views.CustomBackend',
)

# 本站网址
BASE_URL = 'http://127.0.0.1:8000'

# 邮箱发送者  【相关信息查看邮箱服务器的POP3/SMTP/IMAP】
EMAIL_HOST = 'smtp.163.com' # 使用SMTP
EMAIL_PORT = 25
EMAIL_HOST_USER = '18924235915@163.com'
EMAIL_HOST_PASSWORD = 'zyz123'  # 客户端授权密码
EMAIL_USE_TLS = False
EMAIL_FROM = '18924235915@163.com'  # 指明发件人


# 分页配置
PAGINATION_SETTINGS = {
    'PAGE_RANGE_DISPLAYED': 5,     # 当前页附近显示的个数
    'MARGIN_PAGES_DISPLAYED': 2,    # 头和尾附近显示的个数
    'SHOW_FIRST_PAGE_WHEN_INVALID': True,   # 如果按钮失效且不是404时，仅显示首页
}

