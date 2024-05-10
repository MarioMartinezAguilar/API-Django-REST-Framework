from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from django.contrib.auth.models import User
from .serializers import UserSerializer
from rest_framework.generics import ListAPIView, ListCreateAPIView,RetrieveUpdateDestroyAPIView
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny,IsAuthenticated

""" class ListUser(APIView):
    
    def get(self, request, *args, **kwargs):
        user = User.objects.last()
        user_serializer = UserSerializer(user)
        return Response(status=HTTP_200_OK, data=user_serializer.data)
     """

""" class ListUser(ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all() """

class ListUser(ListCreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    #permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer
    queryset = User.objects.all()