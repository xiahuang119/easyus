"""
Django settings for easyus project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

import os
from os.path import abspath, basename, dirname, join, normpath
from sys import path

###### PATH CONFIGURATION
# Absolute filesystem path to the config directory
CONFIG_ROOT = dirname(dirname(abspath(__file__)))

# Absolute filesystem path to the project directory
PROJECT_ROOT = dirname(CONFIG_ROOT)

# Absolute filesystem path to the django repo directory
DJANGO_ROOT = dirname(PROJECT_ROOT)

# Project name
PROJECT_NAME = basename(PROJECT_ROOT).capitalize()

# Project domain
PROJECT_DOMAIN = '%s.com' % PROJECT_NAME.lower()

# Add our project to our python path, this way to don't need to type our project
#name in our dotted import paths
path.append(CONFIG_ROOT)

###### END PATH CONFIGURATION

###### SECURITY CONFIGURATION
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '*$ia#8r0p^sze$1h%m9832ie%r71ldq+4xul4a+n3eu2l0-k2+'

ALLOWED_HOSTS = []
###### END SECURITY CONFIGURATION

###### DEBUG CONFIGURATION
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEST_RUNNER = 'django.test.runner.DiscoverRunner'

TEMPLATE_DEBUG = True
###### END DEBUG CONFIGURATION

###### APP CONFIGURATION
DEFAULT_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

THIRD_PARTY_APPS = ()

PROJECT_APPS = (
    'apps.house',
)

INSTALLED_APPS = DEFAULT_APPS + THIRD_PARTY_APPS + PROJECT_APPS


###### END APP CONFIGURATION

###### MIDDLEWARE CONFIGURATION
MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)
###### END MIDDLEWARE CONFIGURATION

###### URL CONFIGURATION 
ROOT_URLCONF = 'config.urls'
###### END URL CONFIGURATION

###### WSGI CONFIGURATION
WSGI_APPLICATION = 'config.wsgi.application'
###### END WSGI CONFIGURATION

###### DATABASE CONFIGURATION
# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases
#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': os.path.join(DJANGO_ROOT, 'db', 'db.sqlite3'),
#    }
#}
###### END DATABASE CONFIGURATION

###### GENERAL CONFIGURATION
# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

TIME_ZONE = 'America/Los_Angeles'

USE_I18N = True

USE_L10N = True

USE_TZ = True
###### END GENERAL CONFIGURATION

########## TEMPLATE CONFIGURATION
# https://docs.djangoproject.com/en/dev/ref/settings/#template-context-processors
TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.request',
)

# https://docs.djangoproject.com/en/dev/ref/settings/#template-loaders
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

# https://docs.djangoproject.com/en/dev/ref/settings/#template-dirs
TEMPLATE_DIRS = (
    normpath(join(PROJECT_ROOT, 'templates')),
    normpath(join(PROJECT_ROOT, 'extensions')),
)
########## END TEMPLATE CONFIGURATION

########## MEDIA CONFIGURATION
# https://docs.djangoproject.com/en/dev/ref/settings/#media-root
MEDIA_ROOT = normpath(join(PROJECT_ROOT, 'media'))

# https://docs.djangoproject.com/en/dev/ref/settings/#media-url
MEDIA_URL = '/media/'
########## END MEDIA CONFIGURATION

###### STATIC FILES CONFIGURATION
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/
STATIC_ROOT = normpath(join(PROJECT_ROOT, 'public'))

STATIC_URL = '/static/'

STATICFILES_DIRS = (normpath(join(PROJECT_ROOT, 'static')),)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)
###### END STATIC FILES CONFIGURATION

###### LOGIN/LOGOUT CONFIGURATION
LOGIN_REDIRECT_URL = '/'

LOGIN_URL = '/login'

LOGOUT_URL = '/logout/'
###### END LOGIN/LOGOUT CONFIGURATION

########## LOGGING CONFIGURATION
# https://docs.djangoproject.com/en/dev/ref/settings/#logging
LOGGING = {
  'version': 1,
  'disable_existing_loggers': False,
  'filters': {
    'production_only': {
      '()': 'django.utils.log.RequireDebugFalse',
    },
    'development_only': {
      '()': 'django.utils.log.RequireDebugTrue',
    },
  },
  'formatters': {
    'verbose': {
      'format': '[%(asctime)s] %(levelname)-8s [%(name)s:%(lineno)s] %(message)s',
      'datefmt': '%m/%d/%Y %H:%M:%S',
    },
    'simple': {
      'format': '%(levelname)-8s [%(name)s:%(lineno)s] %(message)s',
    },
  },
  'handlers': {
    'null': {
      'level': 'DEBUG',
      'class': 'logging.NullHandler',
    },
    'default': {
      'level': 'DEBUG',
      'class': 'logging.StreamHandler',
    },
    'console_dev': {
      'level': 'DEBUG',
      'filters': ['development_only'],
      'class': 'logging.StreamHandler',
      'formatter': 'simple',
    },
    'console_prod': {
      'filters': ['production_only'],
      'class': 'logging.StreamHandler',
      'formatter': 'simple',
    },
    'file_log': {
      'filters': ['development_only'],
      'class': 'logging.handlers.RotatingFileHandler',
      'filename': join(DJANGO_ROOT, 'logs/app.log'),
      'maxBytes': 1024 * 1024,
      'backupCount': 3,
      'formatter': 'verbose',
    },
    'file_sql': {
      'level': 'DEBUG',
      'filters': ['development_only'],
      'class': 'logging.handlers.RotatingFileHandler',
      'filename': join(DJANGO_ROOT, 'logs/sql.log'),
      'maxBytes': 1024 * 1024,
      'backupCount': 3,
      'formatter': 'verbose',
    },
    'mail_admins': {
      'level': 'ERROR',
      'filters': ['production_only'],
      'class': 'django.utils.log.AdminEmailHandler',
      'include_html': True,
    },
  },
# Catch-all modules that use logging
# Writes to console and file on development, only to console on production
  'root': {
    'handlers': ['console_dev', 'console_prod', 'file_log'],
    'level': 'DEBUG',
  },
  'loggers': {
# Write all SQL queries to a file
    'django.db.backends': {
      'handlers': ['file_sql'],
      'level': 'DEBUG',
      'propagate': False,
    },
# Email admins when 500 error occurs
    'django.request': {
      'handlers': ['mail_admins'],
      'level': 'ERROR',
      'propagate': False,
    },
  }
}
########## END LOGGING CONFIGURATION
