from django.shortcuts import render

# Create your views here.
# users/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate

User = get_user_model()
class RegisterView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        if User.objects.filter(username=username).exists():
            return Response({'error': 'El usuario ya existe'}, status=status.HTTP_400_BAD_REQUEST)
        user = User.objects.create_user(username=username, password=password)
        return Response({'message': 'Usuario creado con éxito'}, status=status.HTTP_201_CREATED)
    
class LoginView(APIView):
    def post(self, request):
        username1 = request.data.get('username')
        password1 = request.data.get('password')

        user = authenticate(username=username1, password=password1)
        if user is not None:
            return Response({'error': 'Loguin correcto, puede pasar'}, status=status.HTTP_200_OK)

        return Response({'message': 'Error de loguin'}, status=status.HTTP_400_BAD_REQUEST)    