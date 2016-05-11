from decouple import config

from .base import BASE_DIR, DEBUG


# URL to serve static files
STATIC_URL = config('STATIC_URL', default='/static/')

# Directories to find static files
STATICFILES_DIRS = [
    BASE_DIR.child('frontend'),
]

# Directories to save media and compiled static files
STATIC_ROOT = BASE_DIR.child('.public', 'static')

# Allow Whitenoise to compress and cache static files
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# URL to serve static files
STATIC_URL = config('STATIC_URL', default='/static/')

# Template finders and processors
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR.child('frontend', 'templates'),
        ],
        'OPTIONS': {
            'debug': DEBUG,
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
