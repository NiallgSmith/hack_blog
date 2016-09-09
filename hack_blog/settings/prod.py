from base import *
import dj_database_url

DATABASES = {
    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


CLEAR_DB_URL = os.environ.get("CLEARDB_DATABASE_URL", "")

DATABASES['default'] = dj_database_url.parse(CLEAR_DB_URL)


STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# DEBUG = True
ALLOWED_HOSTS = ['ns-hack-blog.herokuapp.com']
# SECURITY WARNING: don't run with debug turned on in production!

