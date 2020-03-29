docker-compose -f docker-compose.prod.yml build &&
docker-compose -f docker-compose.prod.yml up -d &&
docker-compose -f docker-compose.prod.yml run web python manage.py makemigrations &&
docker-compose -f docker-compose.prod.yml run web python manage.py migrate &&
docker-compose -f docker-compose.prod.yml run web python manage.py collectstatic --noinput