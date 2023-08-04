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

# Custom User Model Settings for Account
LOGIN_REDIRECT_URL = '/account/dashboard/'
LOGIN_URL = '/account/login/'
AUTH_USER_MODEL = 'account.User'


# Email Settings
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Disabling Password Vallidators
AUTH_PASSWORD_VALIDATORS = []


# Installed App for Project
INSTALLED_APPS += [
    'store',
    'basket',
    'account',
    'payment',
    'orders'
]

STRIPE_ENDPOINT_SECRET = 'whsec_9c427c34dad58e0ea1c0110d73d3759f5a128d1ecdefec6134e55a57b597dfb5'
# PUBLISHABLE_KEY = ''
# SECRET_KEY = ''
# stripe listen --forward-to localhost:8000/payment/webhook/
