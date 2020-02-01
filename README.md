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


### Deploying in Production
To deploy in production, you'll need to change the `docker-compose` config to point to a different environment file. It should include the following env vars:
`
DJANGO_SECRET_KEY=<new secret key>
DJANGO_DEBUG=0
DJANGO_LOG_LEVEL=INFO
`
New secret keys can be generated using https://miniwebtool.com/django-secret-key-generator/
Then simply build and run the app as above.