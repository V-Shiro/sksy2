from __future__ import absolute_import, unicode_literals
import os
# from os import path
from pytz import timezone 

from celery import Celery 
#from django.conf import settings 

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'todo_server.settings')

app = Celery('todo_server')
app.conf.enable_utc = False

app.conf.update(timezone = 'Europe/London')

app.config_from_object('django.conf:settings', namespace = 'CELERY')

#Celery Beat Settings 

app.autodiscover_tasks()

@app.task(bind = True, ignore_result=True)
def debug_task(self):
    print(f'Request: {self.request!r}')