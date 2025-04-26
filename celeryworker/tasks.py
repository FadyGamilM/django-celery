from celery import shared_task


@shared_task
def shared_task():
    print("This is a shared task From celeryworker/views.py")
    return
