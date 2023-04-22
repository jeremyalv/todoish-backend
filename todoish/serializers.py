from rest_framework import serializers
from authentication.serializers import ProfileSerializer
from .models import Task

class TaskSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.ReadOnlyField(source='author.user.username')
    
    description = serializers.CharField(max_length=2000, required=False, allow_blank=True)
    category = serializers.CharField(max_length=50, required=False, allow_blank=True)
    due_date = serializers.DateTimeField(required=False, allow_null=True)

    class Meta:
        model = Task
        fields = '__all__'
        read_only_fields = ['created_at']
    
