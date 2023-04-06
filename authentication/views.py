from django.shortcuts import render
from django.urls import path
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['POST'])
def register(request):
    pass


@api_view(['GET'])
def login(request):
    pass


@api_view(['POST'])
def logout(request):
    pass



