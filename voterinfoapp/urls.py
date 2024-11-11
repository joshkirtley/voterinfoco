from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('view_quizzes/', views.view_quizzes, name='view_quizzes'),
    path('create_quiz/', views.create_quiz, name='create_quiz'),
    path('create_quiz_questions/', views.create_quiz_questions, name='create_quiz_questions'),
    path('edit_question/', views.edit_question, name='edit_question'),
    path('take_quiz', views.take_quiz, name='take_quiz'),
    path('view_quizzes_take', views.view_quizzes_take, name='view_quizzes_take'),
]
