"""
WSGI config for Blog_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os
import sys
path = 'Users\Prashanth\Documents\GitHub\Blog\Blog_project'
if path not in sys.path:
  sys.path.insert(0,path)

#sys.path.append('Users\Prashanth\Documents\GitHub\Blog\Blog_project')

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Blog_project.settings')

application = get_wsgi_application()
