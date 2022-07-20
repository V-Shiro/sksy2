from __future__ import absolute_import, unicode_literals
from asyncio import tasks
import os
import sys
# from os import path
from pytz import timezone

from celery import Celery
from celery.schedules import crontab
from datetime import timedelta

from django.conf import settings
#from django_celery_beat.models import PeriodicTask

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'todo_server.settings')

app = Celery('todo_server')
app.conf.enable_utc = False

app.conf.update(timezone='Europe/Berlin')

app.config_from_object('django.conf:settings', namespace='CELERY')

# Celery Beat Settings

app.conf.beat_schedule = {
    'send_reminder_everyday_at_22': {
        'task': 'todo_server.tasks.notify',
        'schedule': crontab(hour=20, minute=33)
        #"schedule": timedelta(seconds=30),
    }, 

    'updates_reservations_every1min': {
    'task': 'todo_server.tasks.update_slots',
    'schedule': crontab(minute='*/1')

    }

}

app.autodiscover_tasks()


@app.task(bind=True, ignore_result=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
