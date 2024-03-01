from django.urls import path, include
from .views import hello, randomQuiz

urlpatterns = [
    path('hello/', hello),
    path('<int:id>/', randomQuiz),
    
]
