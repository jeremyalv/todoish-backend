from rest_framework import serializers
from django.contrib.auth.models import User

from authentication.models import Profile
from todoish.models import Task

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User()
        fields = '__all__'

class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer()
    # tasks = serializers.HyperlinkedRelatedField(many=True, queryset=Task.objects.all())
    tasks = serializers.HyperlinkedRelatedField(many=True, view_name='task-detail', read_only=True)

    class Meta:
        model = Profile
        fields = ['user', 'tasks']