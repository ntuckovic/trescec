# -*- coding: utf-8 -*-

import os
from base import *
import dj_database_url

DEBUG = False

DEBUG_TOOLBAR = False
CACHE = True
CACHALOT = True

db_from_env = dj_database_url.config(conn_max_age=500)

DATABASES['default'].update(db_from_env)

# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'
