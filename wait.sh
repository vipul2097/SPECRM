#!/bin/sh

while ! nc -z mydb2 3306 ; do
    echo "Waiting for the MySQL Server"
    sleep 3
done

echo "MySQL started"

python3 manage.py makemigrations
python3 manage.py migrate

python3 manage.py runserver 0.0.0.0:8000
