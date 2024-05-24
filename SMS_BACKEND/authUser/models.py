from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='images/students', null=True,blank=True)
    full_name = models.CharField(max_length=150)
    address = models.CharField(max_length=150)
    grade = models.CharField(max_length=2)
    section = models.CharField(max_length=2)
    contact_no = models.CharField(max_length=10)
    roll_no = models.CharField(max_length=999)


class Teacher(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='images/Teachers', null=True,blank=True)
    full_name = models.CharField(max_length=150)
    address = models.CharField(max_length=150)
    contact_no = models.CharField(max_length=10)
    subject = models.CharField(max_length=150)
    level = models.CharField(max_length=150)
    shift = models.CharField(max_length=150,default='Day')


class Staff(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='images/Staff', null=True,blank=True)
    full_name = models.CharField(max_length=150)
    address = models.CharField(max_length=150)
    contact_no = models.CharField(max_length=10)
    position = models.CharField(max_length=150)
    shift = models.CharField(max_length=150,default='Day')