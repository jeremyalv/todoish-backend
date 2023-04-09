from rest_framework import serializers
from django.contrib.auth.models import User
from authentication.models import Profile

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User()
        fields = '__all__'

class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Profile
        fields = '__all__'