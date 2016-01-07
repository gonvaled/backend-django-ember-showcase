"""
WSGI config for backend_django_ember_showcase project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend_django_ember_showcase.settings")

application = get_wsgi_application()

# Use dj-static to serve static files
from dj_static import Cling
application = Cling(application)
