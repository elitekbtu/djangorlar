# Project modules
from settings.base import *


DEBUG = True
ALLOWED_HOSTS = []

# Database configuration
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', 
        'NAME': 'db.sqlite3',
    },
}