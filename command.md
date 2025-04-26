django-admin startproject djangocelery .
pip install celery
pip install redis
pip freeze > requirements.txt
chmod +x ./entrpoint.sh
<!-- to open a shell session inside a container execute this -->
docker exec -it [contaienr-name] /bin/sh
<!-- then to enter the django manage.py shell execute this after you opened a shell session inside the django container -->
./manage.py shell