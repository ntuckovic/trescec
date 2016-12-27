# -*- coding: utf-8 -*-

import os
from base import *
import dj_database_url

DEBUG = True

DEBUG_TOOLBAR = False
CACHE = True
CACHALOT = True
USE_STORAGE = 'aws'

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware'
]

# Update database configuration with $DATABASE_URL.
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

# STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')
STATIC_URL = '/static/'

# STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles/')
# STATICFILES_DIRS = (
#     os.path.join(PROJECT_ROOT, 'static/'),
# )

# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/
STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

if USE_STORAGE is 'dropbox':
    MEDIA_ROOT = '/media'
    DEFAULT_FILE_STORAGE = 'storages.backends.dropbox.DropBoxStorage'
    DROPBOX_OAUTH2_TOKEN = 'i0McIhrQTL0AAAAAAAAA0-49R6XfwiiyaKF0sOCZ9fiQqvStCCQTYyIycBAk19m-'
    DROPBOX_ROOT_PATH = 'trescec'
elif USE_STORAGE is 'aws':
    AWS_ACCESS_KEY_ID = 'AKIAILEUJ6RPNKFSASOA'
    AWS_SECRET_ACCESS_KEY = '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'
    AWS_STORAGE_BUCKET_NAME = 'trescec2'
    AWS_QUERYSTRING_AUTH = False
    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
    AWS_S3_HOST = 's3-eu-west-1.amazonaws.com'
