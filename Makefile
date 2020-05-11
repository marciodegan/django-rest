clean:
    find . -name "*.pyc" -exec rm -rf {} \;

run:
    python manage.py runserver 0.0.0.0:8000
