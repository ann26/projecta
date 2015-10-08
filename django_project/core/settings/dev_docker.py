# -*- coding: utf-8 -*-
from .dev import *  # noqa
import os
print os.environ

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'gis',
        'USER': 'docker',
        'PASSWORD': 'docker',
        'HOST': 'projecta-db',
        'PORT': 5432,
        'TEST_NAME': 'unittests',
    }
}
