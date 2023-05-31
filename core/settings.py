from .default_settings import *

# Project Base Media Settings
import os

# Installed App for Project
INSTALLED_APPS += [
    'store'
]

# Custom Templates Settings
TEMPLATES[0]['DIRS'] = [BASE_DIR / 'templates']


# Project Base Static File Settings
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]
