import os
from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise

from config.settings import STATIC_ROOT

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

application = WhiteNoise(application=get_wsgi_application(), root=STATIC_ROOT)
