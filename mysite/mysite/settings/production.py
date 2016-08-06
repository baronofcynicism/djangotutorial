from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

EBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'djangotutorial',
        'USER': 'django',
        'PASSWORD': 'puppi3s',
        'HOST': '',
        'PORT': ''
    }
}