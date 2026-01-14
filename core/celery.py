from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

app = Celery('core')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'delete-old-car-applications': {
        'task': 'applications.tasks.delete_old_car_applications',
        'schedule': crontab(hour=0, minute=0),
        # 'schedule': crontab(minute='*/1'),  # каждая минута
    }
}

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
