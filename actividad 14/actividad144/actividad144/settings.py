"""
Django settings for actividad144 project.

Generated by 'django-admin startproject' using Django 5.1.6.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path
import sentry_sdk

sentry_sdk.init(
    dsn="https://0e470439ff6e387cde28bd82da27b2a7@o4509086576803840.ingest.us.sentry.io/4509086580932608",
    # Add data like request headers and IP for users,
    # see https://docs.sentry.io/platforms/python/data-management/data-collected/ for more info
    send_default_pii=True,
)

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-7t)d59+(i=a%sg$5io=oja(im_s_m293%h%^)701s#%pbld0ut'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'miapp',  # Asegúrate de agregar tu aplicación aquí
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'actividad144.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'actividad144.wsgi.application'

# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]
HANDLER404 = 'tu_app.views.error_404_view'
# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/
STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Configuración de LOGGING
import os

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'detailed': {
            'format': '{levelname} {asctime} {module} {message}',
            'style': '{',
        },
        'simple': {
            'format': '{levelname} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'diagnostico': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join('logs', 'diagnostico.log'),
            'formatter': 'detailed',
        },
        'auditoria': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': os.path.join('logs', 'auditoria.log'),
            'formatter': 'detailed',
        },
        'seguimiento': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': os.path.join('logs', 'seguimiento.log'),
            'formatter': 'detailed',
        },
        'seguridad': {
            'level': 'WARNING',
            'class': 'logging.FileHandler',
            'filename': os.path.join('logs', 'seguridad.log'),
            'formatter': 'detailed',
        },
        'rendimiento': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': os.path.join('logs', 'rendimiento.log'),
            'formatter': 'detailed',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        },
    },
    'loggers': {
        'diagnostico': {
            'handlers': ['diagnostico', 'console'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'auditoria': {
            'handlers': ['auditoria'],
            'level': 'INFO',
            'propagate': False,
        },
        'seguimiento': {
            'handlers': ['seguimiento'],
            'level': 'INFO',
            'propagate': False,
        },
        'seguridad': {
            'handlers': ['seguridad'],
            'level': 'WARNING',
            'propagate': False,
        },
        'rendimiento': {
            'handlers': ['rendimiento'],
            'level': 'INFO',
            'propagate': False,
        },
    },
}
