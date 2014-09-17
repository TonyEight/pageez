# -*- coding: utf-8 -*-
# Built-in modules
import tempfile
import os
import sys

# Project directory definition.
FS_ENCODING = sys.getfilesystemencoding()
THIS_FILE = __file__.decode(FS_ENCODING)
SETTINGS_DIR = os.path.dirname(os.path.realpath(os.path.abspath(THIS_FILE)))
PROJECT_DIR = os.path.dirname(os.path.realpath(SETTINGS_DIR))
ROOT_DIR = os.path.dirname(os.path.realpath(PROJECT_DIR))
APPS_DIR = os.path.join(ROOT_DIR, 'apps')
TEMP_DIR = tempfile.gettempdir().decode(FS_ENCODING)

# Adds the apps to the pythonpath
sys.path.append(APPS_DIR)

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '&)zjw2024o_o#zo$zk*rg-v!x3^ii-y_7=&!6a$_y)*m4m+g%*'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
TEMPLATE_DEBUG = True
ALLOWED_HOSTS = []


# Application definition
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'pageez.urls'

WSGI_APPLICATION = 'pageez.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
