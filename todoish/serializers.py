from rest_framework import serializers
from authentication.serializers import ProfileSerializer
from .models import Task

class TaskSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.ReadOnlyField(source='author.user.username')

    class Meta:
        model = Task
        fields = '__all__'
        read_only_fields = ['created_at']
    
