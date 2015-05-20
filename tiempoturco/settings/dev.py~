from .base import *

DEBUG = True

TEMPLATE_DEBUG = True
THUMBNAIL_DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1','localhost',]

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'tiempoturco',
        'USER': 'salahaddin',
        'PASSWORD': 'Feyza2015',
        'HOST': 'localhost',
        'PORT': '',
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), "statics", "media")
STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), "statics",  "static_only", )
STATICFILES_DIRS = (os.path.join(os.path.dirname(BASE_DIR), "statics"),)

MEDIA_URL = '/media/'
STATIC_URL = '/static/'

TEMPLATE_DIRS = (
    os.path.join(os.path.dirname(BASE_DIR), "statics", "templates"),
)

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

try:
    from .local import *
except ImportError:
    pass
