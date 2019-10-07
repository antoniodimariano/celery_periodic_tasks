# Periodic task with Celery and Redis as message broker 

A simple example of how to use Celery to schedule periodic tasks. 
It uses Redis as message broker. 


# Periodic Tasks in Celery 

* celery.py = where Celery is initialised 
* celeryconfig.py = all the configuration needed 
* tasks.py = this example implements a simple task that run every 10 seconds


## How to run Celery beat 

` celery -A periodic_tasks beat -l info`

## How to run a worker 

`celery -A periodic_tasks worker -l info`


# Crontab Tasks in Celery 

* celery.py = where Celery is initialised 
* celeryconfig.py = all the configuration needed 
* tasks.py = this example implements a simple notification system that uses Celery's crontab feature

## How to run Celery beat 

` celery -A crontab_tasks beat -l info`

## How to run a worker 

`celery -A crontab_tasks worker -l info`

