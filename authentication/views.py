from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView

from authentication.models import Profile
from authentication.serializers import ProfileSerializer

class Endpoints(APIView):
    def get(self, request, format=None):
        data = ['/users', 'users/:user_id']
        return Response(data)

class ProfileList(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class ProfileDetail(generics.RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
