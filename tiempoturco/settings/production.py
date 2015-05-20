from .base import *

# Disable debug mode

DEBUG = False
TEMPLATE_DEBUG = False
THUMBNAIL_DEBUG = False

ALLOWED_HOSTS = ['.tiempoturco.com', '.tiempoturco.com.']

ADMINS = (
    ('SalahAdDin', 'alagunasalahaddin@live.com'),
)

MANAGERS = ADMINS

#Server's Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'tiempoturco',
        'USER': 'salahaddin',
        'PASSWORD': 'Feyza2015',
        'HOST': '',
        'PORT': '',
        'CONN_MAX_AGE': 1000,
    }
}

#Static Files
MEDIA_ROOT = '/home/salahaddinal/webapps/tiempoturco_static/media'
STATIC_ROOT = '/home/salahaddinal/webapps/tiempoturco_static/static'
STATICFILES_DIRS = (os.path.join(os.path.dirname(BASE_DIR), "statics"),)

MEDIA_URL = '/static/media/'
STATIC_URL = '/static/static/'

TEMPLATE_DIRS = (
    os.path.join(os.path.dirname(BASE_DIR), "statics", "templates"),

)

SESSION_ENGINE = 'django.contrib.sessions.backends.cache'

# Send notification emails as a background task using Celery,
# to prevent this from blocking web server threads
# (requires the django-celery package):
# http://celery.readthedocs.org/en/latest/configuration.html

# import djcelery
#
# djcelery.setup_loader()
#
# CELERY_SEND_TASK_ERROR_EMAILS = True
# BROKER_URL = 'redis://'

CACHE_MIDDLEWARE_ANONYMOUS_ONLY = True

# Use Redis as the cache backend for extra performance
# (requires the django-redis-cache package):
# http://wagtail.readthedocs.org/en/latest/howto/performance.html#cache

# CACHES = {
#     'default': {
#         'BACKEND': 'redis_cache.cache.RedisCache',
#         'LOCATION': '127.0.0.1:6379',
#         'KEY_PREFIX': 'anadolu',
#         'OPTIONS': {
#             'CLIENT_CLASS': 'redis_cache.client.DefaultClient',
#         }
#     }
# }

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

#Web Mail Servers
EMAIL_HOST = 'smtp.webfaction.com'
EMAIL_HOST_USER = 'tiempoturco'
EMAIL_HOST_PASSWORD = 'Feyza2015'
EMAIL_SUBJECT_PREFIX = '[Tiempo Turco]'
DEFAULT_FROM_EMAIL = 'oficial@tiempoturco.com'
SERVER_EMAIL = 'oficial@tiempoturco.com'

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'logfile': {
            'class': 'logging.handlers.WatchedFileHandler',
            'filename': 'error.log'
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        'django': {
            'handlers': ['logfile'],
            'level': 'ERROR',
            'propagate': False,
        },
    }
}


try:
    from .local import *
except ImportError:
    pass
