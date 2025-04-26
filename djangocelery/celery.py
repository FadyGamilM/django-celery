import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangocelery.settings')

# new instance from celery
app = Celery('djangocelery')  # this name is the name of the celery application

# this is the settings file
# read any env stareted with this namespace keyword
app.config_from_object('django.conf:settings', namespace='CELERY')


# define a celery task
@app.task
def add_numbers_task(x: int, y: int) -> int:
    return x + y


# this will automatically discover tasks in the installed apps and looking for a file called tasks.py
app.autodiscover_tasks()
