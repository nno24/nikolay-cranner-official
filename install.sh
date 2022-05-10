#!/bin/bash

pcks="django dj_database_url gunicorn dj3-cloudinary-storage psycopg django-allauth Pillow django-paypal"

for p in $pcks
do
   echo "installing $p"
   pip3 install $p
done

echo "creating requirements"
pip3 freeze --local > requirements.txt
