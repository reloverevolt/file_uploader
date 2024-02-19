.PHONY: clear_migrations

clear_migrations:
	@echo "Clearing migrations..."
	find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
	find . -path "*/migrations/*.pyc" -not -name "__init__.py" -delete
	find . -path "*/migrations/__pycache__/*" -not -name "__init__.py" -delete
	@echo "Migrations cleared."

django_shell:
	docker-compose exec app python manage.py shell_plus

django_test:
	docker-compose exec app python manage.py test

coverage:
	docker-compose run --rm app poetry run coverage run manage.py test files
	docker-compose run --rm app poetry run coverage report

