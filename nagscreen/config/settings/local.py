from .base import *

DEBUG = True

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

MIDDLEWARE += ("debug_toolbar.middleware.DebugToolbarMiddleware",)
INSTALLED_APPS += ("debug_toolbar",)

INTERNAL_IPS = [
    '127.0.0.1',
    '::1'
]