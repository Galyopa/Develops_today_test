from dotenv import load_dotenv

from .base import *

load_dotenv()

# since it's running on my machine, show me the errors
DEBUG = True

SECRET_KEY = os.getenv("SECRET_KEY")

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "postgres",
        "USER": "postgres",
        "PASSWORD": "postgres",
        "HOST": "db",
        "PORT": 5432,
    }
}

# run on every host.
ALLOWED_HOSTS = ["*"]
