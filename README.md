## 350-MA Actions Backend

### Getting Started with Docker

#### Basic Building and Serving
This repository contains a Dockerfile and docker-compose configuration. The docker-compose configuration is based on https://docs.docker.com/compose/django/. To run the app using docker, build with:
`docker-compose build`
and then:
`docker-compose up`

Navigate to `localhost:8000` in your browser to see a list of endpoints, or `localhost:8000/admin` to sign into the admin site. 

#### Running manage.py commands
In order to run commands using `manage.py` with docker-compose, you need to use
`docker-compose run web python manage.py <command-here>`

To get started with the admin site, run
`docker-compose run web python manage.py createsuperuser`
This will allow you to create a login and password.

### Provided Endpoints