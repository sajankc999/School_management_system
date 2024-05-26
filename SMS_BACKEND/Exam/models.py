from django.db import models
from courses.models import *
from authUser.models import Teacher,Student
class Question(models.Model):
    created_date= models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(Teacher,on_delete=models.CASCADE)
    question = models.CharField(max_length=250)
    option_a = models.CharField(max_length=100)
    option_b = models.CharField(max_length=100)
    option_c = models.CharField(max_length=100)
    option_d = models.CharField(max_length=100)
    correct_answer = models.CharField(max_length=100,choices=(('a','a'),('b','b'),('c','c'),('d','d')))
    holding_marks=models.PositiveIntegerField()



class Answer(models.Model):
    answered_by = models.ForeignKey(Student,on_delete=models.CASCADE)
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    answer = models.CharField(max_length=100,choices=(('a','a'),('b','b'),('c','c'),('d','d')))

    

