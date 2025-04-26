FROM python:3.13.3-alpine

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# ensure we are using the updated version of pip 
RUN pip install --upgrade pip

# install dependencies
COPY ./requirements.txt ./usr/src/app/requirements.txt
RUN chmod +x ./usr/src/app/requirements.txt
RUN pip install -r ./usr/src/app/requirements.txt

COPY ./entrypoint.sh ./usr/src/app/entrypoint.sh
RUN chmod +x ./usr/src/app/entrypoint.sh

COPY . .

EXPOSE 8000

ENTRYPOINT [ "/usr/src/app/entrypoint.sh"]