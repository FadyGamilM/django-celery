import os

from celery import Celery

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangocelery.settings')

# new instance from celery
# this name is the name of the celery application
app = Celery('djangocelerystandaloneapp')

# this is the settings file
# read any env stareted with this namespace keyword
app.config_from_object('celeryconfig')
