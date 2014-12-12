"""
WSGI config for easyus project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

import os
from os.path import abspath, dirname
from sys import path

CONFIG_ROOT = dirname(dirname(abspath(__file__)))
path.append(CONFIG_ROOT)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.prod")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
