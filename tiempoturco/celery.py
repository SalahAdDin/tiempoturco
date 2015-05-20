from __future__ import absolute_import

import os

from celery import Celery

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tiempoturco.settings')

from django.conf import settings

app = Celery('tiempoturco',
             broker='amqp://',
             backend='amqp://',
             include=['tiempoturco.tasks'])

# Optional configuration, see the application user guide.
#: Only add pickle to this list if your broker is secured
#: from unwanted access (see userguide/security.html)
app.conf.update(
    CELERY_ENABLE_UTC=True,
    CELERY_TIMEZONE='America/Bogota',
    CELERY_RESULT_BACKEND='djcelery.backends.database:DatabaseBackend',
    CELERY_ACCEPT_CONTENT=['json'],
    CELERY_TASK_SERIALIZER='json',
    CELERY_RESULT_SERIALIZER='json',
)

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))

if __name__ == '__main__':
    app.start()