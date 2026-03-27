from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import APIView
from users.serializers import UserSerializer
from rest_framework.viewsets import ModelViewSet
from users.models import User
from rest_framework.permissions import IsAuthenticated
from users.permissions import IsPostProssessor


# Create your views here.

# class HelloWorldView(APIView):
#     def get(self, request):
#         return Response({'hello': 'world'})

class UserView(ModelViewSet):
    permission_classes = [IsAuthenticated, IsPostProssessor]
    queryset = User.objects.all()
    serializer_class = UserSerializer