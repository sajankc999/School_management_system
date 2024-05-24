from django.db import models
# from django.contrib.auth.models import User
from authUser.models import *
from courses.models import Courses,Batch 

class Assignment(models.Model):
    created_at= models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(Teacher,on_delete=models.CASCADE)
    course = models.ForeignKey(Courses,on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    batch = models.ForeignKey(Batch,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    deadline = models.DateTimeField()

def validate_file_extension(value):
    import os
    from django.core.exceptions import ValidationError
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.pdf', '.doc']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension.')
    
class SubmitAssignment(models.Model):
    assignment = models.ForeignKey(Assignment,on_delete=models.CASCADE)
    submitted_by = models.ForeignKey(Student,on_delete=models.CASCADE) 
    submitted_at= models.DateTimeField(auto_now_add=True)  
    assignment_content = models.FileField(upload_to='assignments/' ,validators=[validate_file_extension])
    remarks = models.TextField()


class CheckAssignment(models.Model):
    submitted_assignment = models.ForeignKey(SubmitAssignment,on_delete=models.CASCADE)
    checked_by = models.ForeignKey(Teacher,on_delete=models.CASCADE)
    checked_date = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    Not_Checked = 'Not Checked'
    Incomplete ='Incomplete'
    Complete ='Complete'
    check_status = ((Not_Checked,'Not Checked'),(Incomplete,'Incomplete'),(Complete,'Complete'))
    is_checked = models.CharField(max_length=55,default=Not_Checked,choices=check_status)
    remarks = models.TextField()

