# Music service with DRF

## Development setup
Install Python 3.7.2

Create a virtual environment: <br/>
`python3 -m venv venv`

To activate a venv: <br/>
`source venv/bin/activate`

Install dependencies: <br/>
`pip install -r requirements.txt`

## Migrate db:
`python3 manage.py makemigrations` <br>
`python3 manage.py migrate`

## Test

`python manage.py test`

## To create an admin account:

`python manage.py createsuperuser`

or

`python manage.py createsuperuser --email admin@example.com --username admin`

## To run server:

`python manage.py runserver`

## Access API

ToDo

## Info

An application inspired by a tutorial on medium.com.