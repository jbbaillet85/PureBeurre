import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'purebeurre',
        'USER': 'purebeurreuser',
        'PASSWORD': os.environ.get("passwordDBPureBeurre"),
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
