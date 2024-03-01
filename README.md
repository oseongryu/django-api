mkdir quiz-backend-test
cd quiz-backend-test
python3 -m venv venv
ls
source venv/bin/activate
pip install django djangorestframework
django-admin startproject myapi .
ls
python manage.py startapp quiz
ls
code .