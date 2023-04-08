from django.db import models
from authentication.models import Profile

class Task(models.Model):
    title = models.CharField(max_length=250)
    description = models.CharField(max_length=2000)
    is_finished = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    category = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.title
    
    class Meta: 
        ordering = ['created_at']

