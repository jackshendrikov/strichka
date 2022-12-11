import dj_database_url

from .base import *

DEBUG = False

ALLOWED_HOSTS = [os.getenv("WEBSITE_HOSTNAME", "*")]

# Password validation.
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

MIDDLEWARE += ["django.middleware.csrf.CsrfViewMiddleware"]

CSRF_COOKIE_SECURE = True
SECURE_REFERRER_POLICY = "same-origin"
SECURE_SSL_REDIRECT = True
SECURE_HSTS_SECONDS = 3600
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

# Redirect swagger through https.
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

# Postgres settings.
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES["default"].update(db_from_env)
