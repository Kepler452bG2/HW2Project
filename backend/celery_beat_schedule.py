from celery.schedules import crontab
from backend.celery_worker import celery_app
from backend.tasks.tasks import fetch_and_save

celery_app.conf.beat_schedule = {
    'fetch-every-day': {
        'task': 'backend.tasks.tasks.fetch_and_save',
        'schedule': crontab(hour=0, minute=0), 
    },
}
