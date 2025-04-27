from celery import Celery
import os


# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangocelery.settings')

# new instance from celery
# this name is the name of the celery application
app = Celery('djangocelerystandaloneapp')

# this is the settings file
# read any env stareted with this namespace keyword
app.config_from_object('celeryconfig')


@app.task
def add_numbers_task(x: int, y: int) -> int:
    return x + y
