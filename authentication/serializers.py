from rest_framework import serializers
from django.contrib.auth.models import User

from authentication.models import Profile
from todoish.models import Task

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User()
        fields = '__all__'

class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    tasks = serializers.PrimaryKeyRelatedField(many=True, queryset=Task.objects.all())

    class Meta:
        model = Profile
        fields = ['user', 'tasks']