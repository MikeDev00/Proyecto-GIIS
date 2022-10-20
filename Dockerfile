# start from an official image
FROM python:3.8

ENV PYTHONUNBUFFERED 1

# arbitrary location choice: you can change the directory
RUN mkdir -p /opt/services/djangoapp/src
WORKDIR /opt/services/djangoapp/src
# install our two dependencies

RUN pip3 install djongo

RUN pip install django-widget-tweaks

RUN pip install mysqlclient  

RUN pip install --upgrade pip gunicorn django

RUN pip install django==3.2

RUN pip install djangorestframework-filters

RUN pip install django-bootstrap-form

RUN pip install flask

RUN pip install django-crispy-forms

RUN pip install django-filter==2.4.0

RUN pip install pytz --upgrade

RUN pip3 install dnspython

RUN pip install tzdata --upgrade

RUN pip install django-utils-six

RUN pip install --upgrade django-cors-headers

RUN pip install pymongo==3.7.2

RUN pip install psycopg2

RUN pip3 install numpy

RUN pip install matplotlib

RUN pip install django-ckeditor
# copy our project code
COPY . /opt/services/djangoapp/src

# expose the port 8000
EXPOSE 8001

# define the default command to run when starting the container
CMD ["gunicorn", "--chdir", "app", "--bind", ":8001", "ProyectoGIIS.wsgi:application"]