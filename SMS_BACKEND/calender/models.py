from django.db import models

# Create your models here.
class Calender(models.Model):
    date = models.DateField()
    event = models.CharField(max_length=150)
    school_holiday = models.BooleanField(default=False)