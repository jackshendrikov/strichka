import logging

from .base import *

DEBUG = True

ALLOWED_HOSTS = ["*"]

# Adjust logging level.
logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
