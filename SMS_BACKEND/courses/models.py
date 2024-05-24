from typing import Iterable
from django.db import models
# from django.contrib.auth.models import User
from authUser.models import *
import datetime
class Courses(models.Model):
    title=models.CharField(max_length=100)
    description = models.TextField()
    duration = models.CharField(max_length=10)
    price = models.IntegerField()
    shift = models.CharField(max_length=100,default='Day')
    taught_by=models.ForeignKey(Teacher,on_delete=models.DO_NOTHING)

    
class MyCourses(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    course = models.ForeignKey(Courses,on_delete=models.CASCADE)
    is_paid = models.BooleanField(default=False)

class Batch(models.Model):
    course = models.ForeignKey(MyCourses,on_delete=models.CASCADE)
    batch = models.CharField(max_length=100,blank=True,null=True)

    def save(self,*args, **kwargs) -> None:
        year = datetime.datetime.now().year
        self.batch = year
        return super(Batch,self).save(*args, **kwargs)





    