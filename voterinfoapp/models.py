from django.db import models

# Create your models here.
class Quiz(models.Model):
    quiz_title = models.CharField(max_length=250)

    class Meta:
        verbose_name_plural = "Quizzes"

    def __str__(self):
        return self.quiz_title

class Question(models.Model):
    question_number=models.IntegerField()
    question=models.CharField(max_length=250)
    a = models.CharField(max_length=250,null=True)
    b = models.CharField(max_length=250,null=True)
    c = models.CharField(max_length=250,null=True)
    d = models.CharField(max_length=250,null=True)
    correct_answer = models.CharField(max_length=250)
    quiz = models.ForeignKey(Quiz,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return '('+str(self.quiz)+') '+str(self.question_number)+'. '+str(self.question)

class Responses(models.Model):

    class Meta:
        verbose_name_plural = "Responses"

    CHOICES = [
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
    ]
    response = models.CharField(
        max_length=250,
        choices=CHOICES,
        default='A',
    )
    question = models.ForeignKey(Question,on_delete = models.CASCADE,null=True)
