from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "0$#kke(6&dt68hf+xhk=&(pi-rp+v&4(1p@ou@izy-=e_qauyi"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get("DEBUG", False)

ALLOWED_HOSTS += os.environ.get("DJANGO_ALLOWED_HOSTS", "").split(" ")

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": os.environ.get("SQL_ENGINE", "django.db.backends.sqlite3"),
        "NAME": os.environ.get("SQL_DATABASE", os.path.join(BASE_DIR, "db.sqlite3")),
        "USER": os.environ.get("SQL_USER", "user"),
        "PASSWORD": os.environ.get("SQL_PASSWORD", "password"),
        "HOST": os.environ.get("SQL_HOST", "localhost"),
        "PORT": os.environ.get("SQL_PORT", "5432"),
        "TEST": {"NAME": "enerlly_test_db"},
    }
}
REDIS_USER = os.environ.get("REDIS_USER", "")
REDIS_PASSWORD = os.environ.get("REDIS_PASSWORD", "")
REDIS_HOST = os.environ.get("REDIS_HOST", "redis_server")
REDIS_PORT = os.environ.get("REDIS_PORT", 6379)
CACHEOPS_REDIS = {
    "host": REDIS_HOST,  # redis-server is on same machine
    "port": REDIS_PORT,  # default redis port
    "db": 1,
    "socket_timeout": 3,  # connection timeout in seconds, optional
    "password": REDIS_PASSWORD,
}

# Cache disabled for local development.
CACHEOPS_ENABLED = False

# Celery connection details for local
CELERY_BROKER_URL = f"redis://{REDIS_USER}:{REDIS_PASSWORD}@{REDIS_HOST}:{REDIS_PORT}"
CELERY_RESULT_BACKEND = f"redis://{REDIS_USER}:{REDIS_PASSWORD}@{REDIS_HOST}:{REDIS_PORT}"

# Health check redis url
REDIS_URL = f"redis://{REDIS_USER}:{REDIS_PASSWORD}@{REDIS_HOST}:{REDIS_PORT}"
