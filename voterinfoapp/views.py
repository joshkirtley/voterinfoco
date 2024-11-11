from django.shortcuts import render,redirect,get_object_or_404,get_list_or_404
from .models import Question,Quiz
from .forms import CreateQuiz,CreateQuestion,EditQuestion,TakeQuiz
from django.forms import formset_factory

# Create your views here.
def home(request):
    return render(request,'home.html')

def view_quizzes(request):
    quizzes = Quiz.objects.all()
    context = {
        'quizzes':quizzes
    }
    return render(request,'view_quizzes.html',context)

def create_quiz(request):
    if request.method == 'GET':
        form = CreateQuiz()
        context = {
            'form':form,
        }
        return render(request,'create_quiz.html',context)
    elif request.method == 'POST':
        form = CreateQuiz(request.POST)
        new_quiz=form.save()
        return redirect('create_quiz_questions',new_quiz.pk)

def create_quiz_questions(request,quiz_pk):
    quiz = get_object_or_404(Quiz,pk=quiz_pk)
    quiz_questions = Question.objects.filter(quiz=quiz).order_by('question_number')
    if request.method == 'GET':
        form = CreateQuestion()
        quiz_title = quiz.quiz_title
        context = {
            'form':form,
            'quiz_questions':quiz_questions,
            'quiz_title':quiz_title
        }
        return render(request,'create_quiz_questions.html',context)
    elif request.method == 'POST':
        form = CreateQuestion(request.POST)
        new_question = form.save(commit=False)
        new_question.quiz = quiz
        new_question.question_number = len(quiz_questions)+1
        new_question.save()
        return redirect('create_quiz_questions',quiz_pk)

def edit_question(request,question_pk):
    question = get_object_or_404(Question,pk=question_pk)
    quiz = question.quiz
    if request.method == 'GET':
        form = EditQuestion(instance=question)
        context = {
            'form':form
        }
        return render(request,'edit_question.html',context)
    elif request.method == 'POST':
        form = EditQuestion(request.POST,instance=question)
        form.save()
        return redirect('create_quiz_questions',quiz.pk)

def take_quiz(request,quiz_pk):
    quiz=get_object_or_404(Quiz,pk=quiz_pk)
    quiz_questions=get_list_or_404(Question,quiz=quiz_pk)
    quiz_questions.sort(key=lambda x:x.question_number,reverse=False)
    quiz_formset=formset_factory(TakeQuiz,extra=len(quiz_questions))
    if request.method == 'GET':
        formset=quiz_formset()
        mylist = zip(quiz_questions,formset)
        context = {
            'formset':formset,
            'quiz':quiz,
            'quiz_questions':quiz_questions,
            'mylist':mylist
        }
        return render(request,'take_quiz.html',context)
    elif request.method == 'POST':
        formset = quiz_formset(request.POST)
        if formset.is_valid():
            index = 0
            for form in formset:
                new_response = form.save(commit=False)
                new_response.question = quiz_questions[index]
                new_response.save()
        return redirect('view_quizzes')

def view_quizzes_take(request):
    quizzes = Quiz.objects.all()
    context = {
        'quizzes':quizzes
    }
    return render(request,'view_quizzes_take.html',context)
