from __future__ import absolute_import

from django.contrib.sitemaps import ping_google
from haystack.management.commands import update_index

from celery import shared_task


@shared_task
def ping():
    ping_google()