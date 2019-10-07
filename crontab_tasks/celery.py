from celery import Celery
from celery.schedules import crontab

app = Celery('crontab_tasks',
             include=['crontab_tasks.tasks'])
app.config_from_object('crontab_tasks.celeryconfig')



app.conf.beat_schedule = {
    "everyday-task": {
        "task": "crontab_tasks.tasks.remember_tasks_to_do",
        "schedule": crontab(hour=7, minute=0)
    }
}
