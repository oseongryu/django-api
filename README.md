## 1. project setting

### init
```bash
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
```

### settings.py
```py
import os
ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'quiz',
    'rest_framework',
]

TIME_ZONE = 'Asia/Seoul'

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
```

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

## 2. hello api 만들기

### serializers.py
```py
from rest_framework import serializers
from .models import Quiz
class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = ('title', 'body', 'answer')
```

### views.py
```py
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Quiz
from .serializers import QuizSerializer
# Create your views here.

@api_view(['GET'])
def helloAPI(request):
    return Response("hellow world!")
```

### urls.py

```py
from django.urls import path, include
from .views import helloAPI

urlpatterns = [
    path('hello/', helloAPI),
]
```

## 3. quiz api

### admin.py

```py
from django.contrib import admin
from .models import Quiz

# Register your models here.
admin.site.register(Quiz)
```

```bash
python manage.py makemigrations
python manage.py migrate
```

## 4. admin

```bash
python manage.py createsuperuser
python manage.py runserver

http://localhost:8000/admin

로그인후 등록

http://localhost:8000/quiz/3
```

```json
[
    {
        "title": "플러터의 타입이 아닌 것은?",
        "body": "String/int/bool/Num",
        "answer": 3
    },
    {
        "title": "넷플릭스 클론 코딩 강의가 올라간 곳은?",
        "body": "아프리카/트위치/유튜브/넷플릭스",
        "answer": 2
    },
    {
        "title": "플러터의 대표적인 상태 관리 기법이 아닌 것은?",
        "body": "vuex/setState()/Provider/BLoC",
        "answer": 0
    },
    {
        "title": "플러터에 대한 설명으로 옳은 것은?",
        "body": "인스타그램이 만들었다/알리바바 앱이 플러터로 만들어졌다/데스크탑 앱은 지원하지 않는다/리액트네이티브 보다 성능이 안좋다",
        "answer": 1
    }
]
```

## 5. deploy

pythonanywhere, heroku
헤로쿠 설치 & 배포 가이드: https://devcenter.heroku.com/articles/getting-started-with-python

```bash
pip install --upgrade pip
pip install django-cors-headers #cors 에러방지
pip install gunicorn #배포를 위한 도구
pip install psycopg2-binary dj-database-url #Heroku postegresql
pip install whitenoise #정적파일사용 미들웨어

pip freeze > requirements.txt
```

settings.py
```py
import dj_database_url

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'django-insecure-oc+f)8v1n&g)6ca3r#2!9=yu6zjgm8gqv8oqhfu87ld349q&_b' )


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'django-insecure-oc+f)8v1n&g)6ca3r#2!9=yu6zjgm8gqv8oqhfu87ld349q&_b' )

db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)
```

### heroku setting
Procfile
runtime.txt

```bash
brew install heroku/brew/heroku
```

### git project
```bash
git init
git add .
git commit -m "commit"
git remote add origin ""
git push -u origin main
```

### HEROKU 가입
```bash
heroku login
heroku create django-api
heroku create oseongryu-django-test
git push heroku master

heroku run python manage.py migrate
heroku run python manage.py createsuperuser
heroku open

appname.herokuapp.com
```

