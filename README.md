# Bit68-Store

## Introduction
It is some APIs let you create many products and retrive them whenever you want.
 
 ### Tech Stack

Our tech stack will include:

* **PostgreSQL** as our database of choice
* **Python3** and **Django** as our server language and server framework
* **Django Rest Framework** for creating and managing APIs 
* **Simple JWT** as our Authanticaton and Authorization third party packege using JWT
  

## Getting Started

### With Out Docker

### Installing Dependencies

#### Python 3.9

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the `/Bit68-Store` directory and running:

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
## API Reference

### Getting Started:

- Base URL: At present this app can only be run locally and is not hosted as a base URL. 
           The backend app is hosted at the default, http://127.0.0.1:5000/, 
           which is set as a proxy in the frontend configuration.
## Endpoints

### POST /signup/
 - General:

Register a new user to the Database.

- Sample: ```curl http://127.0.0.1:8000/api/v1/auth/users/signup/ -X POST -H "Content-Type: application/json" 
    -d {"username":"myname","email":"myemail@gmail.com", "password" : "mypassword"}```
   
                 {
                    "user_data": {
                        "id": 1,
                        "username": "myname",
                        "email": "myemail@gmail.com"
                    },
                    "access_token":  "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjQyMTc2MTkyLCJpYXQiOjE2NDIwODk3OTIsImp0aSI6IjAwMWY2YzBkYjQ2YzQ3YTNiNTMxZmQ4Y2E1MzdiOTlhIiwidXNlcl9pZCI6MX0.FToS3Jh7SfXEsYKAXQDey2H4DLuNoBzXNLFDGtPTrB0",
                    "refresh_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY0MjE3NjE5MiwiaWF0IjoxNjQyMDg5NzkyLCJqdGkiOiJmYmRjZDMxY2Y0MDk0MmNjYWRlZmI0YjY0N2IzYTFmMSIsInVzZXJfaWQiOjF9.JfTcXSM_SSG0tBBSE75RabrKJ1f3mdQfl5HbUhB-jfY"
}

### POST  /login/
 - General:

log an exist user to the App.

- Sample: ```curl http://127.0.0.1:8000/api/v1/auth/users/login/ -X POST -H "Content-Type: application/json" 
    -d {"username":"myname", "password" : "mypassword"}```
   
                 {
                   
                    "access":  "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjQyMTc2MTkyLCJpYXQiOjE2NDIwODk3OTIsImp0aSI6IjAwMWY2YzBkYjQ2YzQ3YTNiNTMxZmQ4Y2E1MzdiOTlhIiwidXNlcl9pZCI6MX0.FToS3Jh7SfXEsYKAXQDey2H4DLuNoBzXNLFDGtPTrB0",
                    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY0MjE3NjE5MiwiaWF0IjoxNjQyMDg5NzkyLCJqdGkiOiJmYmRjZDMxY2Y0MDk0MmNjYWRlZmI0YjY0N2IzYTFmMSIsInVzZXJfaWQiOjF9.JfTcXSM_SSG0tBBSE75RabrKJ1f3mdQfl5HbUhB-jfY"
}
### POST  /refresh/
 - General:

Generate an new access token for the logged in users.

- Sample: ```curl http://127.0.0.1:8000/api/v1/auth/users/refresh/ -X POST -H "Content-Type: application/json" 
    -d {"refresh":"$REFRESH_TOKN"}```
   
                 {
                   
                    "access":  "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjQyMTc2MTkyLCJpYXQiOjE2NDIwODk3OTIsImp0aSI6IjAwMWY2YzBkYjQ2YzQ3YTNiNTMxZmQ4Y2E1MzdiOTlhIiwidXNlcl9pZCI6MX0.FToS3Jh7SfXEsYKAXQDey2H4DLuNoBzXNLFDGtPTrB0",
                    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY0MjE3NjE5MiwiaWF0IjoxNjQyMDg5NzkyLCJqdGkiOiJmYmRjZDMxY2Y0MDk0MmNjYWRlZmI0YjY0N2IzYTFmMSIsInVzZXJfaWQiOjF9.JfTcXSM_SSG0tBBSE75RabrKJ1f3mdQfl5HbUhB-jfY"
}
### POST  /logout/
 - General:

to logged out a logged in user

- Sample: ```curl http://127.0.0.1:8000/api/v1/auth/users/logout/ -X POST -H "Content-Type: application/json" 
    -H "HTTP_AUTHORIZATION : Bearer $ACCESS_TOKEN" ```
   
                 {
                   
                    "message": "Your are logged out!"
                 }
### POST  /products/
 - General:

 let any logged in user add any product to the DB.

- Sample: ```curl http://127.0.0.1:8000/api/v1/products/ -X POST -H "Content-Type: application/json" 
    -H "HTTP_AUTHORIZATION : Bearer $ACCESS_TOKEN" -d {"name":"Infinix gy", "price" : 20899} ```
   
                 {
                "id": 1,
                "seller": {
                    "id": 2,
                    "username": "myname"
                },
                "name": "Infinix gy",
                "price": "20899.00000"
              }
### GET  /products/
 - General:

to get all the products ordered by price from the DB

- Sample: ```curl http://127.0.0.1:8000/api/v1/products/ -X GET -H "Content-Type: application/json" 
    -H "HTTP_AUTHORIZATION : Bearer $ACCESS_TOKEN"  ```
   
                 [
                   {
                       "id": 1,
                       "seller": {
                           "id": 2,
                           "username": "myname"
                       },
                       "name": "Infinix gy",
                       "price": "20899.00000"
                   }
]
### GET  /products/?seller__username=myname
 - General:

to get all the products filtered by specfic seller ordered by price from the DB

- Sample: ```curl http://127.0.0.1:8000/api/v1/products/ -X GET -H "Content-Type: application/json" 
    -H "HTTP_AUTHORIZATION : Bearer $ACCESS_TOKEN"  ```
   
                 [
                   {
                       "id": 1,
                       "seller": {
                           "id": 2,
                           "username": "myname"
                       },
                       "name": "Infinix gy",
                       "price": "20899.00000"
                   }
]
### GET  /products/me/
 - General:

to get all the products that belongs to a specfic user ordered by price from the DB

- Sample: ```curl http://127.0.0.1:8000/api/v1/products/me -X GET -H "Content-Type: application/json" 
    -H "HTTP_AUTHORIZATION : Bearer $ACCESS_TOKEN"  ```
   
              [
                   {
                       "id": 1,
                       "seller": {
                           "id": 2,
                           "username": "myname"
                       },
                       "name": "Infinix gy",
                       "price": "20899.00000"
                   }
        ]
## Author:
### Osama Alagooz
