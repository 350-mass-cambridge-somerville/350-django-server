## 350-MA Actions Backend

### Getting Started with Docker

#### Basic Building and Serving
This repository contains a Dockerfile and docker-compose configuration. The docker-compose configuration is based on https://docs.docker.com/compose/django/. To run the app using docker, build with:
`docker-compose build`
After the first build, you'll need to make and apply migrations and load fixture data. This is described below under `Running manage.py commands - Getting Started`.
and then:
`docker-compose up`

Navigate to `localhost:8000` in your browser to see a list of endpoints, or `localhost:8000/admin` to sign into the admin site. 

#### Running manage.py commands
In order to run commands using `manage.py` with docker-compose, you need to use
`docker-compose run web python manage.py <command-here>`

##### Getting Started
You'll need to create the tables and load some data before you run the app.
Run make migrations commands:
`docker-compose run web python manage.py makemigrations`
Apply migrations:
`docker-compose run web python manage.py migrate`
Load data from fixtures:
`docker-compose run web python manage.py loaddata fixtures/*.json`
Collect static files for admin site:
`docker-compose run web python manage.py collectstatic --noinput`

To get started with the admin site, run
`docker-compose run web python manage.py createsuperuser`
This will allow you to create a login and password.

##### Optional
If you want to dump data, you can use:
`docker-compose run web python manage.py dumpdata --exclude=allauth`

### Provided Endpoints


### Deploying in Production
To deploy in production, you'll need to change the `docker-compose` config to point to a different environment file. It should include the following env vars:
`
DJANGO_SECRET_KEY=<new secret key>
DJANGO_DEBUG=0
DJANGO_LOG_LEVEL=INFO
SQL_ENGINE=django.db.backends.postgresql
SQL_DATABASE=postgres
SQL_HOST=db
SQL_PORT=5433
POSTGRES_USER=actions
POSTGRES_PASSWORD=actions
POSTGRES_DB=$SQL_DATABASE
`
New secret keys can be generated using https://miniwebtool.com/django-secret-key-generator/

In addition, you will need to run 
`docker-compose -f docker-compose.yml -f docker-compose.prod.yml up -d`
to use the production overrides (with certbot).