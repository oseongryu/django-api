# 1. project setting

### init
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

python manage.py makemigrations
python manage.py migrate
python manage.py runserver

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
```
from django.contrib import admin
from .models import Quiz

# Register your models here.
admin.site.register(Quiz)
```
python manage.py makemigrations
python manage.py migrate
