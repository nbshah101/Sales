# Django API with Django Rest Framework

This is on build API with GET, POST, PUT call using Django Rest Framework.
Django REST framework is a powerful and flexible toolkit for building Web APIs.

# Setup

This is requried Django and Djangorestframework of python package

## Installation command

1. pip install Django==1.9
2. pip install djangorestframework


# Run the Server

python manage.py runserver


# URLS to hit on browser:

## Filter by vin, make, model, seller

   http://127.0.0.1:8000/get
   http://127.0.0.1:8000/get/?vin=
   http://127.0.0.1:8000/get/?model=
   http://127.0.0.1:8000/get/?seller=
   filter by vin, make, model, seller

## create sales record
   http://127.0.0.1:8000/sale/

## modify sale record
   http://127.0.0.1:8000/sale/<id>

