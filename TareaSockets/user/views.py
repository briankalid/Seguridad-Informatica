
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from .serializers import User
from .models import user_homework
from rest_framework.response import Response
# Create your views here.

class UserHomework(APIView):
    def post(self,request):
        serializer = User(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status':'ok'}, status = status.HTTP_201_CREATED)
        else:
            return Response({'status':'bad'}, status = status.HTTP_400_BAD_REQUEST)

    def get(self,request):
        try:
            username = request.data['name']
            queryset = user_homework.objects.get(name = username)
            
            if queryset.pswd == request.data['pswd']:
                return Response({ 'status': 'ok' }, status = status.HTTP_200_OK)
            


            return Response({'status':'bad'}, status = status.HTTP_400_BAD_REQUEST)
        except user_homework.DoesNotExist:
            return Response({'status': 'bad', 'error': 'User not found'},status = status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)},status = status.HTTP_400_BAD_REQUEST)
