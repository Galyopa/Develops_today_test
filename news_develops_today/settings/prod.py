# import dj_database_url
# from .base import *
#
# # always set this to false in production
# DEBUG = False
#
# SECRET_KEY = os.environ["SECRET_KEY"]
#
# ALLOWED_HOSTS = ['*']
#
# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.postgresql",
#         "NAME": os.getenv("DB_NAME"),
#         "USER": os.getenv("DB_USER"),
#         "PASSWORD": os.getenv("DB_PASS"),
#         "HOST": os.getenv("DB_HOST", "127.0.0.1"),
#         "PORT": os.getenv("DB_PORT", 5432),
#     }
# }
#
# DATABASES["default"] = dj_database_url.config(conn_max_age=600, ssl_require=True)
#
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True
#
# SECURE_SSL_REDIRECT = True
#
# SESSION_COOKIE_SECURE = True
#
# CSRF_COOKIE_SECURE = True
#
# SECURE_BROWSER_XSS_FILTER = True
#
# SECURE_HSTS_SECONDS = True
#
# SECURE_HSTS_PRELOAD = True
#
# SECURE_HSTS_INCLUDE_SUBDOMAINS = True


import environ

# If using in your own project, update the project namespace below
from base import *

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)

# False if not in os.environ
DEBUG = env('DEBUG')

# Raises django's ImproperlyConfigured exception if SECRET_KEY not in os.environ
SECRET_KEY = env('SECRET_KEY')

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS')

# Parse database connection url strings like psql://user:pass@127.0.0.1:8458/db
DATABASES = {
    # read os.environ['DATABASE_URL'] and raises ImproperlyConfigured exception if not found
    'default': env.db(),
}