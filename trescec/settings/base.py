# -*- coding: utf-8 -*-

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


ALLOWED_HOSTS = [

]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'trescec',
        'USER': 'trescec',
        'PASSWORD': 'trescec',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

# Application definition

INSTALLED_APPS = [
    'suit',
    'imagekit',

    # django core
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.flatpages',

    # 3rd party
    'storages',
    'rest_framework',
    'bootstrapform',
    'suit_ckeditor',
    'ckeditor',
    'ckeditor_uploader',
    'flatblocks',

    'blogs',
    'core',
    'orders',
    'products',
    'flatpages_override'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware'
]

ROOT_URLCONF = 'trescec.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(os.path.dirname(BASE_DIR), 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.static',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'trescec.wsgi.application'


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'hr_HR'

TIME_ZONE = 'Europe/Zagreb'

USE_I18N = True

USE_L10N = True

USE_TZ = True

SITE_ID = 1


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
USE_STORAGE = False

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

CKEDITOR_UPLOAD_PATH = "uploads/"

CKEDITOR_CONFIGS = {
    'awesome_ckeditor': {
        'fontSize_sizes': '8/8px;9/9px;10/10px;11/11px;12/12px;14/14px;16/16px;18/18px;20/20px;22/22px;24/24px;26/26px;28/28px;36/36px;48/48px;72/72px',
        'width': '100%',
        'toolbar': 'full',
        'startupFocus': True,
        'toolbarGroups': [
            {'name': 'document', 'groups': ['mode', 'document', 'doctools']},
            {'name': 'clipboard', 'groups': ['clipboard', 'undo']},
            {'name': 'editing', 'groups': [
                'find', 'selection', 'spellchecker', 'editing']},
            {'name': 'forms', 'groups': ['forms']},
            {'name': 'basicstyles', 'groups': ['basicstyles', 'cleanup']},
            {'name': 'paragraph', 'groups': [
                'list', 'indent', 'blocks', 'align', 'bidi', 'paragraph']},
            {'name': 'links', 'groups': ['links']},
            {'name': 'insert', 'groups': ['insert']},
            {'name': 'styles', 'groups': ['styles']},
            {'name': 'colors', 'groups': ['colors']},
            {'name': 'tools', 'groups': ['tools']},
            {'name': 'others', 'groups': ['others']},
            {'name': 'about', 'groups': ['about']}
        ],
        'removeButtons': ','.join([
            'Flash',
            'ShowBlocks',
            'About',
            'Scayt',
            'TextField',
            'Radio',
            'Checkbox',
            'Form',
            'Textarea',
            'Button',
            'Select',
            'HiddenField',
            'SelectAll',
            'Print',
            'Preview',
            'NewPage',
            'Save',
            'Templates',
            'CreateDiv',
            'Language',
            'BidiRtl',
            'BidiLtr',
            'ImageButton'
        ]),
        'extraPlugins': ','.join([
            'uploadimage'
        ])
    },
}

CKEDITOR_IMAGE_BACKEND = 'pillow'

def ensure_secret_key_file():
    """
    Checks that secret.py exists in settings dir. If not, creates one
    with a random generated SECRET_KEY setting.
    """
    secret_path = os.path.join(BASE_DIR, 'settings', 'secret.py')
    if not os.path.exists(secret_path):
        from django.utils.crypto import get_random_string
        secret_key = get_random_string(
            50, 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)')
        with open(secret_path, 'w') as f:
            f.write("SECRET_KEY = " + repr(secret_key) + "\n")

# import the secret key
ensure_secret_key_file()
from .secret import SECRET_KEY


REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 50
}

# Django Suit configuration
SUIT_CONFIG = {
    # header
    'ADMIN_NAME': 'OPG Treščec',
    # 'HEADER_DATE_FORMAT': 'l, j. F Y',
    # 'HEADER_TIME_FORMAT': 'H:i',

    # forms
    # 'SHOW_REQUIRED_ASTERISK': True,  # Default True
    # 'CONFIRM_UNSAVED_CHANGES': True, # Default True

    # menu
    # 'SEARCH_URL': '/admin/auth/user/',
    # 'MENU_ICONS': {
    #    'sites': 'icon-leaf',
    #    'auth': 'icon-lock',
    # },
    # 'MENU_OPEN_FIRST_CHILD': True, # Default True
    # 'MENU_EXCLUDE': ('auth.group',),
    # 'MENU': (
    #     'sites',
    #     {'app': 'auth', 'icon':'icon-lock', 'models': ('user', 'group')},
    #     {'label': 'Settings', 'icon':'icon-cog', 'models': ('auth.user', 'auth.group')},
    #     {'label': 'Support', 'icon':'icon-question-sign', 'url': '/support/'},
    # ),

    # misc
    # 'LIST_PER_PAGE': 15
}
