django-admin startproject djangocelery .
pip install celery
pip install redis
pip freeze > requirements.txt
chmod +x ./entrpoint.sh
<!-- to open a shell session inside a container  -->
docker exec -it [contaienr-name] /bin/sh