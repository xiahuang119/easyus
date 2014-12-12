"""Production settings and globals."""
from __future__ import absolute_import
from .base import *
import os

########## HOST CONFIGURATION
# https://docs.djangoproject.com/en/1.5/releases/1.5/#allowed-hosts-required-in-production
ALLOWED_HOSTS = [PROJECT_DOMAIN, 'localhost', '127.0.0.1']
########## END HOST CONFIGURATION


########## SECRET CONFIGURATION
# https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
SECRET_KEY = os.environ['SECRET_KEY']
########## END SECRET CONFIGURATION

########## DATABASE CONFIGURATION
# Parse database configuration from $DATABASE_URL
#import dj_database_url
#DATABASES = {}
#DATABASES['default'] = dj_database_url.config()
########## END DATABASE CONFIGURATION

########## TEMPLATE CONFIGURATION
# https://docs.djangoproject.com/en/dev/ref/settings/#template-dirs
TEMPLATE_LOADERS = (
    ('django.template.loaders.cached.Loader', (
       'django.template.loaders.filesystem.Loader',
       'django.template.loaders.app_directories.Loader',
    )),
)
########## END TEMPLATE CONFIGURATION

########## LOGGING CONFIGURATION
# https://docs.djangoproject.com/en/dev/ref/settings/#logging
LOGGERS = {
# Log queue workers to console and file on development
  'rq.worker': {
    'handlers': ['default', 'file_log'],
    'level': 'INFO',
    'propagate': False,
  }
}
LOGGING['loggers'].update(LOGGERS)
########## END LOGGING CONFIGURATION

########## CACHE/QUEUE CONFIGURATION
# https://docs.djangoproject.com/en/dev/ref/settings/#caches
RQ_QUEUES = {}

if 'REDISCLOUD_URL' in os.environ:
import urlparse
redis_url = urlparse.urlparse(os.environ['REDISCLOUD_URL'])

CACHES = {
  'default': {
    'BACKEND': 'django_redis.cache.RedisCache',
    'LOCATION': '%s:%s:%s' % (redis_url.hostname, redis_url.port, 0),
    'OPTIONS': {
      'PASSWORD': redis_url.password
    }
  }
}

RQ_QUEUES = {
  'default': {
    'USE_REDIS_CACHE': 'default'
  },
  'high': {
    'USE_REDIS_CACHE': 'default'
  },
  'low': {
    'USE_REDIS_CACHE': 'default'
  }
}
RQ_SHOW_ADMIN_LINK = True
SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'
########## END CACHE/QUEUE CONFIGURATION


