"""Development settings and globals"""

from __future__ import absolute_import
from .base import *
import os

###### DEBUG CONFIGURATION
DEBUG=True

TEMPLATE_DEBUG = DEBUG
###### END DEBUG CONFIGURATION

###### DATABASE CONFIGURATION                                                   
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases                 
DATABASES = {
    'default': {
         'ENGINE': 'django.db.backends.sqlite3',                                 
         'NAME': os.path.join(DJANGO_ROOT, 'db', 'db.sqlite3'),                  
     }                                                                           
}                                                                               
###### END DATABASE CONFIGURATION

###### MEDIA CONFIGURATION
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media')

###### CACHE CONFIGURATION
CACHE_ENGINES = {
    'redis': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'localhost:6379:0',
    },
    'dummy': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}

CACHES = {
    'redis': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'localhost:6379:0',
    }
}
CACHES['default'] = CACHE_ENGINES[os.getenv('CACHE', 'dummy')]
SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'
###### END CACHE CONFIGURATION

###### REDIS QUEUE CONFIGURATION
"""
RQ_QUEUES = {
  'default': {
    'USE_REDIS_CACHE': 'redis'
  },
  'high': {
    'USE_REDIS_CACHE': 'redis'
  },
  'low': {
    'USE_REDIS_CACHE': 'redis'
  }
}
RQ_SHOW_ADMIN_LINK = True
"""
########## END REDIS QUEUE CONFIGURATION

########## LOGGING CONFIGURATION
# https://docs.djangoproject.com/en/dev/ref/settings/#logging
LOGGERS = {
# Log requests locally without [INFO] tag
  'werkzeug': {
    'handlers': ['default'],
    'level': 'DEBUG',
    'propagate': False,
  },
# Log queue workers to console and file on development
  'rq.worker': {
    'handlers': ['default', 'file_log'],
    'level': 'DEBUG',
    'propagate': False,
  },
}
LOGGING['loggers'].update(LOGGERS)
########## END LOGGING CONFIGURATION
