from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import UserAbs
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken

@api_view(['POST'])
def criar_usuario(request):
    username = request.data.get('username')
    password = request.data.get('password')
    email = request.data.get('email')
    telefone = request.data.get('telefone')

    if not username or not password:
        return Response({'Erro': 'informacao insuficiente'}, status=status.HTTP_400_BAD_REQUEST)
    
    if UserAbs.objects.filter(username = username).exists():
        return Response({'Erro': 'Username ja existe'}, status=status.HTTP_400_BAD_REQUEST)
    
    if UserAbs.objects.filter(email = email).exists():
        return Response({'Erro': 'email ja existe'}, status=status.HTTP_400_BAD_REQUEST)

    usuario = UserAbs.objects.create_user(
        username= username,
        password= password,
        email= email,
        telefone = telefone
    )
    return Response({'Criou seu usuario aenticado! Parabenssssss'}, status=status.HTTP_201_CREATED)

@api_view(['POST'])
def logar_usuario_token(request):
    usuario = request.data.get('username')
    senha = request.data.get('password')

    user = authenticate(username=usuario, password=senha)

    if user:
        refresh = RefreshToken.for_user(user)
        return Response({
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        },status=status.HTTP_200_OK)
    else:
        return Response({'Error": "Credenciais inválidas'}, status=status.HTTP_401_UNAUTHORIZED)
