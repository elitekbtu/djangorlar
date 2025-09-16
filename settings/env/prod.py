# Project modules
from settings.base import *


DEBUG = False
ALLOWED_HOSTS = ["lcoalhost"]

# Database configuration
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', 
        'NAME': 'db.sqlite3',
    },
}