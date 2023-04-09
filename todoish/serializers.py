from rest_framework import serializers
from authentication.serializers import ProfileSerializer
from .models import Task

# class TaskSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(required=True, max_length=250)
#     description = serializers.CharField(required=False, allow_blank=True, max_length=2000)
#     is_finished = serializers.BooleanField(required=True)
#     created_at = serializers.DateTimeField(autonowadd?)
#     updated_at = serializers.DateTimeField()
#     # author =
#     category = serializers.CharField(max_length=50)

#     def create(self, validated_data):
#         """
#         Create and return a new Task instance, based on validated_data
#         """
#         return Task.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
#         """
#         Update and return an existing Task instance, based on validated_data
#         """
#         instance.title = validated_data.get('title', instance.title)
#         instance.description = validated_data.get('description', instance.description)
#         instance.is_finished = validated_data.get('is_finished', instance.is_finished)
#         instance.created_at = validated_data.get('created_at', instance.created_at)
#         instance.updated_at = validated_data.get('updated_at', instance.updated_at)
#         # instance.author
#         instance.category = validated_data.get('category', instance.category)

#         instance.save()
#         return instance

class TaskSerializer(serializers.ModelSerializer):
    author = ProfileSerializer(required=True)

    class Meta:
        model = Task
        fields = '__all__'
        read_only_fields = ['created_at']






