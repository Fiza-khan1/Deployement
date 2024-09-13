"""
WSGI config for DatabaseChannel project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""
import os
from django.core.wsgi import get_wsgi_application

# Set the default settings module for the 'django' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DatabaseChannel.settings')

# Create a WSGI application object for the Django project.
application = get_wsgi_application()
os.environ["DJANGO_SETTINGS_MODULE"] = "{{ DatabaseChannel }}.settings"
import os

os.environ["DJANGO_SETTINGS_MODULE"] = "DatabaseChannel.settings"

from django.contrib.auth.handlers.modwsgi import check_password

from django.core.handlers.wsgi import WSGIHandler

application = WSGIHandler()
# If you need to wrap the application with a custom WSGI middleware, do it here.
# Ensure that HelloWorldApplication is correctly defined and imported.
# from helloworld.wsgi import HelloWorldApplication
# application = HelloWorldApplication(application)

