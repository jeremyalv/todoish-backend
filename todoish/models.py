from django.db import models
from authentication.models import Profile

class Task(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='tasks')

    title = models.CharField(max_length=250)
    description = models.CharField(max_length=2000, blank=True)
    category = models.CharField(max_length=50, blank=True)
    
    is_finished = models.BooleanField(default=False)
    due_date = models.DateTimeField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta: 
        ordering = ['created_at']

    def __str__(self) -> str:
        return self.title
    
  