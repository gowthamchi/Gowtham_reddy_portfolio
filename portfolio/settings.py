import os
from pathlib import Path
from django.contrib.messages import constants as messages
from dotenv import load_dotenv
load_dotenv() 

# BASE DIRECTORY
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY SETTINGS
SECRET_KEY = 'your-secret-key'
DEBUG = False
ALLOWED_HOSTS = ['gowtham-reddy-portfolio-1.onrender.com']

# INSTALLED APPS (Including all necessary apps)
INSTALLED_APPS = [  
    'django.contrib.staticfiles',# Required for serving static files
    'django.contrib.messages',
    'django.contrib.sessions',
    'main',  # Main portfolio app
]

# MIDDLEWARE CONFIGURATION
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',    
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    "django.contrib.messages.middleware.MessageMiddleware",
]


# URL CONFIGURATION
ROOT_URLCONF = 'portfolio.urls'

# TEMPLATE CONFIGURATION
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                #'django.contrib.auth.context_processors.auth',
                 'django.contrib.messages.context_processors.messages',
                #'django.template.context_processors.media',
            ],
        },
    },
]

# WSGI CONFIGURATION
WSGI_APPLICATION = 'portfolio.wsgi.application'

# DATABASE CONFIGURATION (Using SQLite for simplicity)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}

MIGRATION_MODULES = {
    app: None for app in INSTALLED_APPS
}

# LANGUAGE AND TIMEZONE SETTINGS
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# STATIC & MEDIA FILE CONFIGURATION
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'main/static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# WhiteNoise config
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# 📤 Email Backend Settings
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 465
EMAIL_USE_TLS = False
EMAIL_USE_SSL = True


EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')    # ✅ App password (not your Gmail login!)
ALLOWED_HOSTS = ['dinesh-portfolio-hjg3.onrender.com', 'localhost', '127.0.0.1']



MESSAGE_STORAGE = 'django.contrib.messages.storage.cookie.CookieStorage'

MESSAGE_TAGS = {
    messages.DEBUG: 'debug',
    messages.INFO: 'info',
    messages.SUCCESS: 'success',
    messages.WARNING: 'warning',
    messages.ERROR: 'danger',  # Use 'danger' if you're using Bootstrap for red alerts
}
