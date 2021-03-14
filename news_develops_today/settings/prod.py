import dj_database_url
from .base import *

# always set this to false in production
DEBUG = False

SECRET_KEY = os.environ["SECRET_KEY"]

ALLOWED_HOSTS = ['*']

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("DB_NAME"),
        "USER": os.getenv("DB_USER"),
        "PASSWORD": os.getenv("DB_PASS"),
        "HOST": os.getenv("DB_HOST", "127.0.0.1"),
        "PORT": os.getenv("DB_PORT", 5432),
    }
}

DATABASES["default"] = dj_database_url.config(conn_max_age=600, ssl_require=True)

EMAIL_PORT = 587
EMAIL_USE_TLS = True

SECURE_SSL_REDIRECT = True

SESSION_COOKIE_SECURE = True

CSRF_COOKIE_SECURE = True

SECURE_BROWSER_XSS_FILTER = True

SECURE_HSTS_SECONDS = True

SECURE_HSTS_PRELOAD = True

SECURE_HSTS_INCLUDE_SUBDOMAINS = True
