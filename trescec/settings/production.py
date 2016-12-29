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

SECRET_KEY = os.environ['SECRET_KEY']

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = os.environ['EMAIL_HOST_USER']
EMAIL_HOST_PASSWORD = os.environ['EMAIL_HOST_PASSWORD']
EMAIL_PORT = 587

SHOP_SYSTEM_EMAIL = 'shop@opg-trescec.hr'
SHOP_ADMIN_EMAILS = ['ntuckovic@gmail.com']
SHOP_CONTACT_EMAILS = SHOP_ADMIN_EMAILS

if USE_STORAGE is 'dropbox':
    MEDIA_ROOT = '/media'
    DEFAULT_FILE_STORAGE = 'storages.backends.dropbox.DropBoxStorage'
    DROPBOX_OAUTH2_TOKEN = os.environ['DROPBOX_OAUTH2_TOKEN']
elif USE_STORAGE is 'aws':
    AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
    AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
    AWS_STORAGE_BUCKET_NAME = 'trescec2'
    AWS_QUERYSTRING_AUTH = False
    AWS_S3_HOST = 's3-eu-west-1.amazonaws.com'
    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
