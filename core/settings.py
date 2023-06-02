from .default_settings import *

# Project Base Media Settings
import os


# Custom Templates Settings
TEMPLATES[0]['DIRS'] = [BASE_DIR / 'templates']

# Custom Context Processor Settings
TEMPLATES[0]['OPTIONS']['context_processors'].append(
    'store.context_processors.categories')
TEMPLATES[0]['OPTIONS']['context_processors'].append(
    'basket.context_processors.basket')

# Project Base Static File Settings
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

# Project Base Media Settings
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

# Installed App for Project
INSTALLED_APPS += [
    'store',
    'basket'
]
