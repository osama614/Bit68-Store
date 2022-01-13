# Bit68-Store

## Introduction
It is some APIs let you create many products and retrive them whenever you want.
 
 ### Tech Stack

Our tech stack will include:

* **PostgreSQL** as our database of choice
* **Python3** and **Django** as our server language and server framework
* **Django Rest Framework** for creating and managing APIs 
* **Simple JWT** as our Authanticaton and Authorization third party packege using JWT

### Main Files: Project Structure

  
##Overall:
* Models are located in the `models.py`.
* Controllers are also located in `app.py`.
* The web frontend is located in `templates/`, which builds static assets deployed to the web server at `static/`.
* Web forms for creating data are located in `form.py`

## Getting Started

### With Out Docker

### Installing Dependencies

#### Python 3.9

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the `/casting_agency_app` directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Django](https://www.djangoproject.com/)  is a high-level Python web framework that encourages rapid development and clean, pragmatic design.

- [rest_framework](https://www.django-rest-framework.org/) is a powerful and flexible toolkit for building Web APIs.

- [rest_framework_simplejwt](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/) Simple JWT provides a JSON Web Token authentication backend for the Django REST Framework.  
- [django-cors-headers](https://pypi.org/project/django-cors-headers/) is the extension we'll use to handle cross origin requests from our frontend server.


#### Running the server

From within the `/Bit68-Store` directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
python manage.py runserver
```
 
#### Database Migrations
With Postgres running, setup a database schema using the Django ORM file provided. From the `/Bit68-Store` folder in terminal run:
```bash
python manage.py migrate
or
./manage.py migrate
```
#### Testing
to run the tests of the app. From the `/Bit68-Store` folder in terminal run: 

```bash
python manage.py test
or
./manage.py test <app_name> to test each app alone.
```

### With Docker  
From the `/Bit68-Store` folder in terminal run:
```bash
docker-compose build
```
this to build your images for Django and Postgres

then,
run:

```bash
docker-compose up -d
```
to start up your containers

now I supposed that you can find the app running on [localhost|http://127.0.0.1:8000/](http://127.0.0.1:8000/)
then, 
go to your app working directory on the container to run any commend that you need by run:

```bash
docker exec -it django_app_container bash
```
now you can migrate your database from `/Bit68-Store` directory by run:
```bash
python manage.py migrate
or
./manage.py migrate
```
and tests by run:
```bash
python manage.py test
or
./manage.py test <app_name> to test each app alone.
```
