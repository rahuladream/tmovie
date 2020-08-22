import os
from celery import Celery
from django.apps import apps

from .celerybeat_schedule import CELERYBEAT_SCHEDULE

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tmovie.settings.local')

app = Celery('tmovie_tasks')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace="CELERY")

# Load task modules from all registered Django app configs.
app.autodiscover_tasks(lambda: [n.name for n in apps.get_app_configs()])

app.conf.update(CELERYBEAT_SCHEDULE=CELERYBEAT_SCHEDULE)
