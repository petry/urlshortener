# -*- coding: utf-8 -*-
# Autor: Marcos Daniel Petry - <marcospetry@gmail.com>
import os
PROJECT_ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Marcos Daniel Petry', 'marcospetry@gmail.com'),
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'data.sqlite',                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}


TIME_ZONE = 'America/Sao_Paulo'

LANGUAGE_CODE = 'pt-BR'

SITE_ID = 1

USE_I18N = True

USE_L10N = True

MEDIA_ROOT = os.path.join(PROJECT_ROOT_PATH, "media")

MEDIA_URL = '/media/'

ADMIN_MEDIA_PREFIX = MEDIA_URL+'admin/'

SECRET_KEY = '*7cx=ja*o=t2jl97hs&&oo0c7k95k@zjcst_#pl*6f$z3f95)-'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.core.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    'django.contrib.messages.context_processors.messages',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',

)

ROOT_URLCONF = 'urlshortener.urls'

TEMPLATE_DIRS = (
    os.path.join(PROJECT_ROOT_PATH, "templates"),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.humanize',
    'django.contrib.admin',
    
    'shorturl',
    'account',
    
)
SITE_ID = 2

LOGIN_REDIRECT_URL = '/'

LOGIN_URL = '/u/login/'

DEFAULT_FROM_EMAIL = 'example@example.com.br'

if DEBUG:
    # python -m smtpd -n -c DebuggingServer localhost:1025
    EMAIL_BACKEND = 'django.core.mail.backends.dummy.EmailBackend'
    EMAIL_HOST = 'localhost'
    EMAIL_PORT = 1025
else:
    SERVER_EMAIL = 'xxx@gmail.com.br'
    EMAIL_HOST = 'smtp.gmail.com'
    EMAIL_PORT = 587
    EMAIL_HOST_USER = 'xxx@gmail.com.br'
    EMAIL_HOST_PASSWORD = 'xxx'
    EMAIL_USE_TLS = True


