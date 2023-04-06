from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def endpoints(request):
    data = ['/users', 'users/:task_id']

    return Response(data)

