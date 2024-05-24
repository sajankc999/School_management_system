from django.db import models

class NoticeBoard(models.Model):
    title = models.CharField(max_length=100)
    context = models.TextField()
    created_at= models.DateTimeField(auto_now_add=True)
