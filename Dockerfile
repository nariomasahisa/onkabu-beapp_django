FROM python:3.9

WORKDIR /app
COPY . /app

RUN apt-get install
RUN apt-get update
RUN pip install --upgrade pip
RUN pip install django
RUN pip install djangorestframework
RUN pip install mysqlclient
RUN pip install boto3

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]