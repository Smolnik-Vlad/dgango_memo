create_users:
	python manage.py shell -c "from django.contrib.auth.models import User; User.objects.bulk_create([User.objects.create_user(username='user' + str(i), password='password') for i in range(1,21)])"
migrate:
	python manage.py makemigrations
	python manage.py migrate

createsuperuser:
	python manage.py createsuperuser --username=$(shell cat .env | grep DJANGO_SU_NAME | cut -d '=' -f2) --email=$(shell cat .env | grep DJANGO_SU_EMAIL | cut -d '=' -f2)

runserver:
	python manage.py runserver

shell:
	python manage.py shell