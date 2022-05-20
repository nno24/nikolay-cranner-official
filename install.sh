#!/bin/bash

pcks="django dj_database_url gunicorn  psycopg2-binary django-allauth Pillow boto3 django-storages"

for p in $pcks
do
   echo "installing $p"
   pip3 install $p
done

echo "creating requirements"
pip3 freeze --local > requirements.txt
