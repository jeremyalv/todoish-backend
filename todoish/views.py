from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User

from rest_framework import status, generics, permissions
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse

from authentication.models import Profile
from todoish.models import Task
from todoish.serializers import TaskSerializer

class APIRoot(APIView):
    def get(self, request, format=None):
        return Response({
            'users': reverse('user-list', request=request, format=format),
            'tasks': reverse('task-list', request=request, format=format),
        })

class Endpoints(APIView):
    def get(self, request, format=None):
        data = ['/tasks', 'tasks/:task_id']
        return Response(data)

# TODO This view is too abstracted, to be refactored into regular APIView-Inherited view
class TaskList(generics.ListCreateAPIView):
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    # Associate the task with a Profile 
    def perform_create(self, serializer):
        serializer.save(author=self.get_profile(self.request))

    def get_profile(self, request):
        profile = Profile.objects.get(user=request.user)
        return profile

class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    queryset = Task.objects.all()
    serializer_class = TaskSerializer

