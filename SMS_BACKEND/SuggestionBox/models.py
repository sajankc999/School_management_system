from django.db import models
from django.contrib.auth.models import User

class SuggestionBox(models.Model):
    created_by = models.ForeignKey(User,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    




