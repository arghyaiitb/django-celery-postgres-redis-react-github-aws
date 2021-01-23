from celery.schedules import crontab

from backend.celery import app
from backend.celery import task


@app.on_after_finalize.connect
def setup_periodic_tasks(sender, **kwargs):
    # this would send the request every 2 hours 52 min. Read more about the config below.
    # https://docs.celeryproject.org/en/stable/userguide/periodic-tasks.html#crontab-schedules
    sender.add_periodic_task(crontab(minute=52, hour="*/2"), test.s("world"))


@task
def test(data):
    print(data)

