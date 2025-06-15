from celery import Celery
from celery.schedules import crontab

celery_app = Celery(
    'backend',
    broker='redis://redis:6379/0',
    backend='redis://redis:6379/0',
    include=['backend.tasks.tasks']
)

celery_app.conf.beat_schedule = {
    'fetch-daily': {
        'task': 'backend.tasks.tasks.fetch_and_save',
        'schedule': crontab(hour=8, minute=0),
    },
}
