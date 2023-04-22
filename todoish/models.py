from django.db import models
from authentication.models import Profile

class Task(models.Model):
    title = models.CharField(max_length=250)
    description = models.CharField(max_length=2000)
    is_finished = models.BooleanField(default=False)
    due_date = models.DateTimeField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='tasks', null=False)
    category = models.CharField(max_length=50)

    class Meta: 
        ordering = ['created_at']

    def __str__(self) -> str:
        return self.title
    
  