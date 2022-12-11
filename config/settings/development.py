import logging
import mimetypes
import socket

from .base import *

DEBUG = True

ALLOWED_HOSTS = ["*"]

# Setup for using debug panel inside docker.
hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
INTERNAL_IPS = [ip[:-1] + "1" for ip in ips] + ["127.0.0.1", "10.0.2.2"]

INSTALLED_APPS += ["debug_toolbar", "template_timings_panel"]
MIDDLEWARE = ["debug_toolbar.middleware.DebugToolbarMiddleware"] + MIDDLEWARE

# Email settings.
EMAIL_HOST = "localhost"
EMAIL_PORT = "1025"

DEBUG_TOOLBAR_PANELS = [
    "debug_toolbar.panels.versions.VersionsPanel",
    "debug_toolbar.panels.timer.TimerPanel",
    "debug_toolbar.panels.settings.SettingsPanel",
    "debug_toolbar.panels.headers.HeadersPanel",
    "debug_toolbar.panels.request.RequestPanel",
    "debug_toolbar.panels.sql.SQLPanel",
    "debug_toolbar.panels.staticfiles.StaticFilesPanel",
    "debug_toolbar.panels.templates.TemplatesPanel",
    "debug_toolbar.panels.cache.CachePanel",
    "debug_toolbar.panels.signals.SignalsPanel",
    "debug_toolbar.panels.logging.LoggingPanel",
    "debug_toolbar.panels.redirects.RedirectsPanel",
    "template_timings_panel.panels.TemplateTimings.TemplateTimings",
]

DEBUG_TOOLBAR_CONFIG = {
    "RESULTS_CACHE_SIZE": 15,
    "SQL_WARNING_THRESHOLD": 200,
    "INTERCEPT_REDIRECTS": False,
}

# Fix error with JS file.
mimetypes.add_type("application/javascript", ".js", True)

# Adjust logging level.
logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
