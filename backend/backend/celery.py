import os

from celery import Celery

celery_env = "$CELERY_ENVIRONMENT"
celery_settings_value = "backend.settings.local" if celery_env.endswith("CELERY_ENVIRONMENT") else celery_env
os.environ.setdefault("DJANGO_SETTINGS_MODULE", celery_settings_value)

app = Celery("backend")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()

task = app.task


@app.task(bind=True)
def debug_task(self, data):
    print(data)
