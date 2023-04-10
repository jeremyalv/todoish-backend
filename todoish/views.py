from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.decorators import api_view

from authentication.models import Profile
from todoish.models import Task
from todoish.serializers import TaskSerializer

@api_view(['GET'])
def endpoints(request):
    data = ['/tasks', 'tasks/:task_id']

    return Response(data)

@method_decorator(csrf_exempt, name='dispatch')
class TaskList(APIView):
    """
    List all tasks, or create a new task
    """

    def get(self, request, format=None):
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)

        return Response(serializer.data)
    
    def post(self, request, format=None):
        data = request.data

        # Directly create Task object using Task model
        task = Task.objects.create(
            title=data['title'],
            description=data['description'],
            is_finished=data['is_finished'],
            category=data['category'],

            # To serialize nested objects, in the view we must retrieve the nested object
            author=self.get_profile(data['author_id']),
        )

        serializer = TaskSerializer(task, many=False)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def get_profile(self, pk):
        user = User.objects.get(pk=pk)
        profile = Profile.objects.get(user=user)

        return profile

@method_decorator(csrf_exempt, name='dispatch')
class TaskDetail(APIView):
    """
    Retrieve, update, or delete a Task instance
    """

    def get_object(self, pk):
        try:
            return Task.objects.get(pk=pk)
        except Task.DoesNotExist:
            raise Http404
    
    def get(self, request, pk, format=None):
        task = self.get_object(pk)
        serializer = TaskSerializer(task)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        data = request.data

        task = self.get_object(pk)

        task.title = data['title']
        task.description = data['description']
        task.is_finished = data['is_finished']
        task.category = data['category']
        # To serialize nested objects, in the view we must retrieve the nested object
        task.author = self.get_profile(data['author_id'])

        # Save updated changes
        task.save()
        
        serializer = TaskSerializer(task, many=False)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk, format=None):
        task = self.get_object(pk)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def get_profile(self, pk):
        user = User.objects.get(pk=pk)
        profile = Profile.objects.get(user=user)

        return profile
