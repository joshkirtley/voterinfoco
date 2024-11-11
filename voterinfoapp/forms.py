from django.forms import ModelForm,RadioSelect
from django import forms
from .models import Quiz,Question,Responses

class CreateQuiz(ModelForm):
    class Meta:
        model = Quiz
        fields = ['quiz_title']

class CreateQuestion(ModelForm):
    class Meta:
        model = Question
        exclude = ['quiz','question_number']

class EditQuestion(ModelForm):
    class Meta:
        model = Question
        fields = '__all__'

class TakeQuiz(ModelForm):
    class Meta:
        model = Responses
        exclude = ['question']
        widgets = {
            'response':RadioSelect(),
        }
