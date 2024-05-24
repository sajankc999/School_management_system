from django.db import models
# from django.contrib.auth.models import User
from authUser.models import Student
class Result(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    course = models.CharField(max_length=100)
    marks_recieved = models.CharField(max_length=100)
    pass_statues = models.BooleanField(default=True)
    marks_sheet = models.ImageField(upload_to='images/results')
