import os

# ! => ARCH CONFIGURATIONS
CELERY_BROKER_URL = os.environ.get(
    'CELERY_BROKER_URL', 'redis://redis:6379/0')
# redis -> refering to the protocol
# redis -> refering to the hostname of the redis server
# :6379 -> refering to the port of the redis server
# 0 -> refering to the database number (as redis supports multiple databases around 16)

CELERY_RESULT_BACKEND = os.environ.get(
    'CELERY_RESULT_BACKEND', 'redis://redis:6379/0')
