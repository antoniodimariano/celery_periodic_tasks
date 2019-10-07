from celery import Celery
from celery.schedules import crontab

app = Celery('periodic_tasks',
             include=['periodic_tasks.tasks'])
app.config_from_object('periodic_tasks.celeryconfig')



app.conf.beat_schedule = {
    "run-me-every-ten-seconds": {
        "task": "periodic_tasks.tasks.check",
        "schedule": 10.0
    }
}
