from .base import *

DEBUG = False

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": get_env_variable('NAGSCREEN_DB_NAME'),
        "USER": get_env_variable('NAGSCREEN_DB_USER'),
        "PASSWORD": get_env_variable('NAGSCREEN_DB_PASSWORD'),
        "HOST": "localhost",
        "PORT": "",
    }
}

ALLOWED_HOSTS = ['*']