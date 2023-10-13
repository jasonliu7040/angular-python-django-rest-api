"""
WSGI config for  project.

This module contains the WSGI application used by Django's development server
and any production WSGI deployments. It should expose a module-level variable
named ``application``. Django's ``runserver`` and ``runfcgi`` commands discover
this application via the ``WSGI_APPLICATION`` setting.

Usually you will have the standard Django WSGI application here, but it also
might make sense to replace the whole Django WSGI application with a custom one
that later delegates to the Django one. For example, you could introduce WSGI
middleware here, or combine a Django application with an application of another
framework.

"""
import os
import sys

from django.core.wsgi import get_wsgi_application
from configurations import importer

# make sure that encoding is to utf-8
reload(sys)
sys.setdefaultencoding('utf8')

# We defer to a DJANGO_SETTINGS_MODULE already in the environment. This breaks
# if running multiple sites in the same mod_wsgi process. To fix this, use
# mod_wsgi daemon mode with each site in its own daemon process, or use
# os.environ["DJANGO_SETTINGS_MODULE"] = ".settings"
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings.production")
os.environ.setdefault("DJANGO_CONFIGURATION", "Production")

importer.install()

# This checks if the env file is there
# to auto load your env variables.
try:
    import dotenv
    ROOT_DIR = os.path.dirname(__file__)
    dotenv.load_dotenv(os.path.join(ROOT_DIR, ".env"))
except ImportError:
    pass


# This application object is used by any WSGI server configured to use this
# file. This includes Django's development server, if the WSGI_APPLICATION
# setting points here.
application = get_wsgi_application()

# Apply WSGI middleware here.
# from helloworld.wsgi import HelloWorldApplication
# application = HelloWorldApplication(application)
