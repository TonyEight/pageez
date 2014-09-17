# -*- coding: utf-8 -*-
# Development settings for pageez project
from pageez.settings.base import *

# Databases settings
DATABASES = {
    'default': {
        # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        # Or path to database file if using sqlite3.
        'NAME': 'pageez',
        # The following settings are not used with sqlite3:
        'USER': 'pageez',
        'PASSWORD': 'pageez',
        # Empty for localhost through domain sockets or '127.0.0.1'
        # for localhost through TCP.
        'HOST': '',
        # Set to empty string for default.
        'PORT': '',
    }
}

INSTALLED_APPS += (
    'debug_toolbar',
)

# Media definitions
MEDIA_ROOT = os.path.join(PROJECT_DIR, 'media')
MEDIA_URL = '/media/'
STATIC_ROOT = os.path.join(PROJECT_DIR, 'static')